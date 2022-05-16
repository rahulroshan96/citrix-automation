import argparse
import sys
from citrix.utils import constants


class Argument:
    def __init__(self):
        self.my_parser = None
        self.username = None
        self.password = None
        self.ip_address = None
        self.protocol = None
        self.input_file = None
        self.output_file = None
        self.debug = False
        self.command = None
        self.args = None

    def has_output_file(self):
        return True if self.output_file else False

    def has_input_file(self):
        return True if self.input_file else False

    def validate(self):
        count = 0
        for arg in vars(self.args):
            if getattr(self.args, arg):
                if arg == constants.INPUT_FILE:
                    self.input_file = getattr(self.args, arg)
                    continue
                if arg == constants.OUTPUT_FILE:
                    self.output_file = getattr(self.args, arg)
                    continue
                if arg == 'debug':
                    self.debug = True
                    continue
                if arg == constants.IP_ADDRESS:
                    self.ip_address = getattr(self.args, arg)
                    continue
                if arg == constants.PROTOCOL:
                    if getattr(self.args, arg) not in [constants.HTTP, constants.HTTPS]:
                        print("Protocol %s is not supported" % str(arg))
                        sys.exit(1)
                    self.protocol = getattr(self.args, arg)
                    continue
                if arg == constants.USERNAME:
                    self.username = getattr(self.args, arg)
                    continue
                if arg == constants.PASSWORD:
                    self.password = getattr(self.args, arg)
                    continue
                if count == 1:
                    print("Multiple resources operations are not supported")
                    sys.exit(1)
                if getattr(self.args, arg):
                    count = count + 1
                    self.command = arg
        if not self.username:
            print("username is not provided")
            sys.exit(1)
        if not self.password:
            print("password is not provided")
            sys.exit(1)
        if not self.ip_address:
            print("ip_address is not provided")
            sys.exit(1)


    def set_arguments(self):
        self.my_parser = argparse.ArgumentParser(description='List of Commands')

        self.my_parser.add_argument('--list-vips', action='store_true',
                                    help="List all VIPs with services and servicegroups "
                                         "bindings")
        self.my_parser.add_argument('--list-all-certs', action='store_true', help="Lists all the certs")
        self.my_parser.add_argument('--list-expired-certs', action='store_true', help="Lists all the expired certs")

        self.my_parser.add_argument('--list-stale-vips', action='store_true', help="List all the VIPs not bounded "
                                                                                   "to any services/SGs")

        self.my_parser.add_argument('--list-down-vips', action='store_true', help="List all the down vips")

        self.my_parser.add_argument('--list-stale-services', action='store_true',
                                    help="List all the Services not bounded to any VIP")
        self.my_parser.add_argument('--list-stale-servers', action='store_true',
                                    help="List all the Servers not bounded to any Service")
        self.my_parser.add_argument('--list-stale-service-groups', action='store_true',
                                    help="List all ServiceGroups not bounded to any VIP")

        self.my_parser.add_argument('--delete-vips', action='store_true',
                                    help="Delete all VIPs and bounded services and "
                                         "servicegroups, from input file")
        self.my_parser.add_argument('--delete-stale-vips', action='store_true',
                                    help="Delete all VIPs and bounded services and "
                                         "servicegroups, from input file")
        self.my_parser.add_argument('--delete-stale-services', action='store_true',
                                    help="Delete all Services not bounded to any VIPs, provide input file for "
                                         "selected deletion")
        self.my_parser.add_argument('--delete-stale-service-groups', action='store_true',
                                    help="Delete all ServiceGroups not bounded to any VIPs, provide input file for "
                                         "selected deletion")
        self.my_parser.add_argument('--delete-stale-servers', action='store_true',
                                    help="Delete all servers not bounded to any services, provide input file for "
                                         "selected deletion")
        self.my_parser.add_argument('--create-vip', action='store_true',
                                    help="Create VIP")
        self.my_parser.add_argument('--delete-vip-with-expired-certs', action='store_true',
                                    help="Delete all VIPs bouded to expired certificates")
        self.my_parser.add_argument('--delete-expired-certs', action='store_true',
                                    help="Delete All the expired certificates")
        self.my_parser.add_argument('--input-file', action='store', type=str, help="Input file with name of VIPs")
        self.my_parser.add_argument('--output-file', action='store', type=str, help="Output file name")
        self.my_parser.add_argument('--ip-address', action='store', type=str, help="Citrix Server IP Address")
        self.my_parser.add_argument('--protocol', action='store', type=str, help="http/https")
        self.my_parser.add_argument('--username', action='store', type=str, help="Citrix Server Username")
        self.my_parser.add_argument('--password', action='store', type=str, help="Citrix Server Password")

        self.args = self.my_parser.parse_args()
        self.validate()

        return self

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_ip_address(self):
        return self.ip_address

    def get_protocol(self):
        return self.protocol
