from .resource import Resource
import traceback
from nitro.resource.config.cs.cspolicy import cspolicy


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
        return cspolicy.get(self.client)

    def delete(self, policy_name):
        try:
            service_obj = cspolicy.get(self.client, policy_name)
            result = cspolicy.delete(self.client, service_obj)
            self.logger.info('Policy "%s" Deleted Successfully' % policy_name)
        except Exception as e:
            self.logger.error(traceback.print_exc())
            raise e