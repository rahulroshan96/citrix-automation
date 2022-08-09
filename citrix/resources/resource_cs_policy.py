from .resource import Resource
import traceback
from nitro.resource.config.cs.cspolicy import cspolicy
from nitro.resource.config.cs.cspolicy_csvserver_binding import cspolicy_csvserver_binding
# {'_policyname': 'test01-gold', '_domain': 'CS-5740-PROD-BI-RPT-RIG-01-REDIR', '_stateflag': '128', '_action': 'VIP-5740-SITEDOWN', '_priority': '100', '_hits': '0', '_pihits': '0', '_pipolicyhits': '0'}
from citrix.utils.utils import get_pagination_all

class CSPolicy(Resource):
    def __init__(self, client, logger):
        self.client = client
        self.logger = logger

    def list_by_name(self):
        result = []
        for policy in self.list_by_object():
            result.append(policy.policyname)
        return result

    def list_by_object(self):
        self.logger.info("Gathering Policies..Please Wait...")
        return get_pagination_all(cspolicy, self.client)

    def delete(self, policy_name):
        try:
            service_obj = cspolicy.get(self.client, policy_name)
            result = cspolicy.delete(self.client, service_obj)
            self.logger.info('Policy "%s" Deleted Successfully' % policy_name)
        except Exception as e:
            self.logger.error(traceback.print_exc())
            raise e

    def get_cspolicy_lbserver_binding(self, cspolicy_name):
        try:
            return cspolicy_csvserver_binding.get(self.client, cspolicy_name)
        except Exception as e:
            self.logger.error(traceback.print_exc())
            return None