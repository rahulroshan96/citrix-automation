from core.controller import Controller
from resources.ct_client import get_client
from resources.resource_vip import VIP
from resources.resource_service import Service
from resources.resource_service_group import ServiceGroup
from resources.resource_ssl_cert_key import SSLCertKey
from resources.resource_server import Server
from resources.resource_cs_policy import CSPolicy
from resources.resource_cs_vserver import CSVServer
from resources.resource_cs_action import CSAction
from utils import constants
from utils import utils
import csv


class Builder:
    def __init__(self):
        self.logger = None
        self.input_file = None
        self.output_file = None
        self.client = None
        self.worker = None
        self.backup_file = None
        self.restore_file = None
        self.args = None
        self.vip_client = None
        self.sg_client = None
        self.svc_client = None
        self.ssl_cert_client = None
        self.server_client = None
        self.cs_policy_client = None
        self.cs_vserver_client = None
        self.cs_action = None
        self.controller = None
        self.result = None

    def setup_resource_clients(self):
        self.vip_client = VIP(self.client, self.logger)
        self.sg_client = ServiceGroup(self.client, self.logger)
        self.svc_client = Service(self.client, self.logger)
        self.ssl_cert_client = SSLCertKey(self.client, self.logger)
        self.server_client = Server(self.client, self.logger)
        self.cs_policy_client = CSPolicy(self.client, self.logger)
        self.cs_vserver_client = CSVServer(self.client, self.logger)
        self.cs_action = CSAction(self.client, self.logger)
        return self

    def set_args(self, args):
        self.args = args
        return self

    def set_logger(self, logger):
        self.logger = logger
        return self

    def set_client(self):
        ip_address = self.args.get_ip_address()
        protocol = self.args.get_protocol()
        username = self.args.get_username()
        password = self.args.get_password()
        if protocol:
            self.client = get_client(self.logger, ip_address, username, password, protocol)
        else:
            self.client = get_client(self.logger, ip_address, username, password)
        return self

    def build(self):
        # this returns Controller object
        self.controller = Controller(self.client, self.vip_client, self.sg_client, self.svc_client, \
                                     self.ssl_cert_client, self.server_client, self.cs_policy_client, \
                                     self.cs_vserver_client, self.cs_action, self.logger)
        return self

    def get_configuration(self):
        # all the resources clients must be created first
        # this will set the Configuration object
        return self

    def execute(self):
        '''
        This will figure out which function to execute
        :return:
        '''
        if self.args.command == constants.LIST_VIPS:
            self.result = self.controller.list_vips()
        elif self.args.command == constants.LIST_DOWN_VIPS:
            self.result = self.controller.list_down_vips()
        elif self.args.command == constants.LIST_STALE_VIPS:
            self.result = self.controller.list_stale_vips()
        elif self.args.command == constants.LIST_ALL_CERTS:
            self.result = self.controller.list_cert_keys()
        elif self.args.command == constants.LIST_EXPIRED_CERTS:
            self.result = self.controller.list_expired_certs()
        elif self.args.command == constants.LIST_STALE_SERVICES:
            self.result = self.controller.list_stale_services()
        elif self.args.command == constants.LIST_STALE_SERVICE_GROUPS:
            self.result = self.controller.list_stale_sg()
        elif self.args.command == constants.LIST_STALE_SERVERS:
            self.result = self.controller.list_stale_servers()
        elif self.args.command == constants.DELETE_STALE_SERVERS:
            self.result = self.controller.delete_stale_servers()
        elif self.args.command == constants.DELETE_STALE_SERVICES:
            self.result = self.controller.delete_stale_services()
        elif self.args.command == constants.DELETE_STALE_SERVICE_GROUPS:
            self.result = self.controller.delete_stale_service_groups()
        elif self.args.command == constants.DELETE_EXPIRED_CERTS:
            self.result = self.controller.delete_expired_certs()
        elif self.args.command == constants.DELETE_VIPS:
            self.result = self.controller.delete_vips(self.read_input())
        elif self.args.command == constants.DELETE_STALE_VIPS:
            self.result = self.controller.delete_vips(self.read_input())
        elif self.args.command == constants.DELETE_VIP_WITH_EXPIRED_CERTS:
            self.result = self.controller.delete_vips_with_expired_certs()

    def read_input(self):
        if self.args.has_input_file():
            input_data = utils.read_input_file(self.args.input_file, self.logger)
            if len(input_data) > 0:
                return input_data
        return None

    def save_output(self):
        if self.result and self.args.has_output_file():
            with open(self.args.output_file, "w") as f:
                writer = csv.writer(f)
                writer.writerows(self.result)
