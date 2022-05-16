from .resource import Resource
import traceback
from nitro.resource.config.lb.lbvserver import lbvserver
from nitro.resource.config.lb.lbvserver_service_binding import lbvserver_service_binding
from nitro.resource.config.lb.lbvserver_servicegroup_binding import \
    lbvserver_servicegroup_binding
from citrix.utils import constants


class VIP(Resource):
    def __init__(self, client, logger):
        self.client = client
        self.logger = logger

    def list_by_name(self):
        result = []
        vips = self.list_vips_by_object()
        for vip in vips:
            result.append([vip.name])
        return result

    def list_vips_by_object(self):
        return lbvserver.get(self.client)

    def delete(self, vip_name):
        try:
            vip_obj = lbvserver.get(self.client, vip_name)
            result = lbvserver.delete(self.client,vip_obj)
            self.logger.info('VIP "%s" Deleted Successfully' % vip_name)
        except Exception as e:
            self.logger.error(str(e))
            self.logger.error(traceback.print_exc())

    def list_down_vips(self):
        result = []
        for vip in self.list_vips_by_object():
            if vip.curstate.lower() == constants.VIP_STATUS_DOWN:
                result.append([vip.name])
        return result

    def get_services_bounded_to_vip(self, vip_name):
        service_list = []
        try:
            services_list = lbvserver_service_binding.get(self.client, vip_name)
            for service in services_list:
                if service.servicename != None:
                    service_list.append(service.servicename)
        except Exception as e:
            self.logger.error(str(e))
        return service_list

    def get_sg_bounded_to_vip(self, vip_name):
        service_groups_list = []
        try:
            obj_list = lbvserver_servicegroup_binding.get(self.client, vip_name)
            for obj in obj_list:
                if obj.servicegroupname is not None:
                    service_groups_list.append(obj.servicegroupname)
        except Exception as e:
            self.logger.error(str(e))
        return service_groups_list

    def vip_not_bound_to_sg_and_svc(self, vip_name):
        if not self.get_sg_bounded_to_vip(vip_name) and not self.get_services_bounded_to_vip(
                vip_name):
            return True
        return False

    def create_vip(self):
        import pdb;pdb.set_trace()
        new_vip = lbvserver()
        new_vip.name = "testVIP123"
        new_vip.servicetype = "http"
        result = lbvserver.add(self.client,new_vip)
        self.logger.info("hello")


