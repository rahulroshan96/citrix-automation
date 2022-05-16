from citrix.resources.resource_vip import VIP
from citrix.resources.resource_service import Service
from citrix.resources.resource_service_group import ServiceGroup
from citrix.resources.resource_ssl_cert_key import SSLCertKey
from citrix.resources.resource_server import Server
from citrix.resources.resource_cs_policy import CSPolicy
from citrix.resources.resource_cs_vserver import CSVServer
from citrix.resources.resource_cs_action import CSAction
from citrix.utils import utils
import concurrent.futures
from alive_progress import alive_bar


class Controller:
    def __init__(self, client, vip_client: VIP, sg_client: ServiceGroup, service_client: Service, \
                 ssl_cert_client: SSLCertKey, server_client: Server, cs_policy_client: CSPolicy, \
                 cs_vserver_client: CSVServer, cs_action: CSAction, logger):
        self.client = client
        self.vip_client = vip_client
        self.sg_client = sg_client
        self.service_client = service_client
        self.ssl_cert_client = ssl_cert_client
        self.server_client = server_client
        self.cs_policy_client = cs_policy_client
        self.cs_vserver_client = cs_vserver_client
        self.cs_action = cs_action
        self.vip_to_cs_objs_action_object = {}
        self.logger = logger

    def list_vips(self):
        result = self.vip_client.list_by_name()
        for vip in result:
            self.logger.info(vip[0])
        return result

    def list_down_vips(self):
        result = self.vip_client.list_down_vips()
        for vip in result:
            self.logger.info(vip[0])
        return result

    def list_stale_vips(self):
        result = []
        all_vips = self.vip_client.list_by_name()
        self.logger.info("Stale VIPs are:")
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            with alive_bar(len(all_vips)) as bar:
                for vip in all_vips:
                    vip_name = vip[0]
                    future = executor.submit(self.vip_client.vip_not_bound_to_sg_and_svc, vip_name)
                    if future.result():
                        self.logger.info(vip_name)
                        result.append(vip)
                    bar()
        return result

    def list_cert_keys(self):
        result = self.ssl_cert_client.list_by_name()
        self.logger.info("SSL Cert Keys are:")
        for ssl_certkey in result:
            self.logger.info(ssl_certkey[0])
        return result

    def list_expired_certs(self):
        result = self.ssl_cert_client.list_expired_certs()
        self.logger.info("Expired SSL Certs are:")
        for ssl_cert in result:
            self.logger.info(ssl_cert[0])
        return result

    def list_stale_services(self):
        stale_services = []
        result = set()
        all_vips = self.vip_client.list_by_name()
        all_servies = set(self.service_client.list_by_name())
        used_services = set()
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            with alive_bar(len(all_vips)) as bar:
                for vip in all_vips:
                    vip_name = vip[0]
                    future = executor.submit(self.vip_client.get_services_bounded_to_vip, vip_name)
                    used_services_by_vip = future.result()
                    used_services.update(set(used_services_by_vip))
                    bar()
        result = all_servies - used_services
        self.logger.info("Stale Services are:")
        for svc in list(result):
            stale_services.append([svc])
            self.logger.info(svc)
        return stale_services

    def list_stale_sg(self):
        stale_sgs = []
        result = set()
        all_vips = self.vip_client.list_by_name()
        all_sgs = set(self.sg_client.list_by_name())
        used_sgs = set()
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            with alive_bar(len(all_vips)) as bar:
                for vip in all_vips:
                    vip_name = vip[0]
                    future = executor.submit(self.vip_client.get_sg_bounded_to_vip, vip_name)
                    used_sgs_by_vip = future.result()
                    used_sgs.update(set(used_sgs_by_vip))
                    bar()
        result = all_sgs - used_sgs
        self.logger.info("Stale Service Groups are:")
        for sg in list(result):
            stale_sgs.append([sg])
            self.logger.info(sg)
        return stale_sgs

    def list_stale_servers(self):
        result = []
        all_stale_servers = set()
        used_server_names = set()
        all_servers = self.server_client.list_by_object()
        all_services = self.service_client.list_by_object()
        for service_obj in all_services:
            if hasattr(service_obj, 'servername'):
                used_server_names.add(service_obj.servername)
        for server_obj in all_servers:
            if server_obj.name not in used_server_names:
                all_stale_servers.add(server_obj.name)
        self.logger.info("Stale Servers are:")
        for svc in list(all_stale_servers):
            self.logger.info(svc)
            result.append([svc])
        return result

    def delete_stale_servers(self):
        '''
        TODO: need to test this one, on real deletion
        :return:
        '''
        stale_servers = self.list_stale_servers()
        if len(stale_servers) and utils.ask_before_run(self.logger):
            with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
                with alive_bar(len(stale_servers)) as bar:
                    for svc in stale_servers:
                        server_name = svc[0]
                        future = executor.submit(self.server_client.delete, server_name)
                        future.result()
                        bar()

    def delete_stale_services(self):
        stale_services = self.list_stale_services()
        if len(stale_services) and utils.ask_before_run(self.logger):
            with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
                with alive_bar(len(stale_services)) as bar:
                    for stale_service in stale_services:
                        service_name = stale_service[0]
                        future = executor.submit(self.service_client.delete, service_name)
                        future.result()
                        bar()

    def delete_stale_service_groups(self):
        stale_sgs = self.list_stale_sg()
        if len(stale_sgs) and utils.ask_before_run(self.logger):
            with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
                with alive_bar(len(stale_sgs)) as bar:
                    for stale_sg in stale_sgs:
                        sg_name = stale_sg[0]
                        future = executor.submit(self.sg_client.delete, sg_name)
                        future.result()
                        bar()

    def delete_expired_certs(self):
        stale_certs = self.list_expired_certs()
        if len(stale_certs) and utils.ask_before_run(self.logger):
            with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
                with alive_bar(len(stale_certs)) as bar:
                    for stale_cert in stale_certs:
                        cert_name = stale_cert[0]
                        future = executor.submit(self.ssl_cert_client.delete, cert_name)
                        future.result()
                        bar()

    def get_vip_to_cs_objs_action_object_mapping(self):
        for policy in self.cs_policy_client.list_by_object():
            if hasattr(policy, '_action') and policy._action and policy._action != "":
                action_object = self.cs_action.get(policy._action)
                if hasattr(action_object,
                           '_targetlbvserver') and action_object._targetlbvserver and action_object._targetlbvserver != "":
                    if not self.vip_to_cs_objs_action_object.get(action_object._targetlbvserver):
                        self.vip_to_cs_objs_action_object[action_object._targetlbvserver] = {"cs_action_list": [],
                                                                                        "cs_policy_list": []}

                    self.vip_to_cs_objs_action_object[action_object._targetlbvserver]["cs_policy_list"].append(policy)
                    self.vip_to_cs_objs_action_object[action_object._targetlbvserver]["cs_action_list"].append(action_object)
        actions = self.cs_action.list_by_object()
        for action in actions:
            if hasattr(action, "_targetlbvserver"):
                action_object = self.cs_action.get(action._name)
                if not self.vip_to_cs_objs_action_object.get(action._targetlbvserver):
                    self.vip_to_cs_objs_action_object[action._targetlbvserver] = {"cs_action_list": [],
                                                                                  "cs_policy_list": []}
                self.vip_to_cs_objs_action_object[action._targetlbvserver]["cs_action_list"].append(action_object)

    def policy_and_action_cleanup(self, vip_name):
        if self.vip_to_cs_objs_action_object.get(vip_name):
            try:
                self.delete_all_policy_for_target_vip(vip_name)
                self.logger.info("CS Policy deleted for vip %s", vip_name)
            except:
                pass
            try:
                self.delete_all_action_for_target_vip(vip_name)
                self.logger.info("CS Action deleted for vip %s", vip_name)
            except:
                pass

    def delete_all_action_for_target_vip(self, vip_name):
        if self.vip_to_cs_objs_action_object.get(vip_name):
            for action_obj in self.vip_to_cs_objs_action_object.get(vip_name)["cs_action_list"]:
                try:
                    self.cs_action.delete(action_obj.name)
                    self.logger.info("Context-Switching actions deleted for vip_name %s" % vip_name)
                except Exception as e:
                    self.logger.error("Failed to Delete context-switching action %s for vip_name %s: %s" % (
                        action_obj, vip_name, str(e)))

    def delete_all_policy_for_target_vip(self, vip_name):
        if self.vip_to_cs_objs_action_object.get(vip_name):
            for policy_obj in self.vip_to_cs_objs_action_object.get(vip_name)["cs_policy_list"]:
                try:
                    self.cs_vserver_client.delete_csvserver_cs_policy_binding(policy_obj.policyname)
                    self.cs_policy_client.delete(policy_obj.policyname)
                    self.logger.info("Context-Switching policy deleted for vip_name %s" % vip_name)
                except Exception as e:
                    self.logger.error("Failed to Delete context-switching policy %s for vip_name %s: %s" % (
                        policy_obj.policyname, vip_name, str(e)))

    def delete_vips(self, vips_list=None):
        result = []
        delete_vips_list = vips_list if vips_list else []
        if not vips_list:
            delete_vips_list = self.vip_client.list_by_name()
        if len(delete_vips_list) > 0:
            self.logger.info("VIPs to be deleted are:")
            for vip_name in delete_vips_list:
                self.logger.info(vip_name)
            self.get_vip_to_cs_objs_action_object_mapping()
            self.logger.info(self.vip_to_cs_objs_action_object)
            if utils.ask_before_run(self.logger):
                with alive_bar(len(delete_vips_list)) as bar:
                    for vip_name in delete_vips_list:
                        self.policy_and_action_cleanup(vip_name)
                        self.cs_vserver_client.unbind_csvip_policy_delete_policy(vip_name)
                        self.vip_client.delete(vip_name)
                        bar()
        else:
            self.logger.info("No VIPs available for deletion")
        for vip in delete_vips_list:
            result.append([vip])
        return result

    def delete_stale_vips(self, vips_list=None):
        result = []
        delete_vips_list = vips_list if vips_list else []
        if not vips_list:
            delete_vips_list = self.list_stale_vips()
        if len(delete_vips_list) > 0:
            self.delete_vips(delete_vips_list)
        for vip in delete_vips_list:
            result.append([vip])
        return result

    def delete_vips_with_expired_certs(self):
        vips_to_be_deleted_set = set()
        vips_to_be_deleted_list = []
        expired_certs = self.ssl_cert_client.list_expired_certs()
        for cert in expired_certs:
            cert_name = cert[0]
            vips_to_be_deleted_set.update(set(self.ssl_cert_client.get_certkeys_vip_binding_list(cert_name)))
        self.delete_vips(list(vips_to_be_deleted_set))
        for vip in list(vips_to_be_deleted_set):
            vips_to_be_deleted_list.append([vip])
        return vips_to_be_deleted_list

    def create_new_vip(self):
        self.vip_client.create_vip()
