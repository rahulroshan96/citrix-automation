from .resource import Resource
import traceback
from nitro.resource.config.ssl.sslcertkey import sslcertkey
from nitro.resource.config.ssl.sslcertkey_binding import sslcertkey_binding
from citrix.utils import constants

class SSLCertKey(Resource):
    def __init__(self, client, logger):
        self.client = client
        self.logger = logger

    def list_by_name(self):
        result = []
        for ssl_key in self.list_by_object():
            result.append([ssl_key.certkey])
        return result

    def list_by_object(self):
        return sslcertkey.get(self.client)

    def list_expired_certs(self):
        result = []
        for cert in self.list_by_object():
            if cert.status == constants.CERT_STATUS_EXPIRED:
                result.append([cert.certkey])
        return result

    def delete(self, cert_name):
        try:
            cert_obj = sslcertkey.get(self.client, cert_name)
            result = sslcertkey.delete(self.client, cert_obj)
            self.logger.info('Cert "%s" Deleted Successfully' % cert_name)
        except Exception as e:
            self.logger.error(str(e))
            self.logger.error(traceback.print_exc())

    def get_certkeys_vip_binding_list(self, cert_key_name):
        all_vips_names = []
        try:
            result = sslcertkey_binding.get(self.client, cert_key_name)
            if result.sslcertkey_sslvserver_bindings:
                for vip in result.sslcertkey_sslvserver_bindings:
                    all_vips_names.append(vip['servername'])
        except Exception as e:
            pass
        return all_vips_names
