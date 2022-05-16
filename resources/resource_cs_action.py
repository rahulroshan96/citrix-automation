from .resource import Resource
import traceback
from nitro.resource.config.cs.csaction import csaction

class CSAction(Resource):
    def __init__(self, client, logger):
        self.client = client
        self.logger = logger

    def list_by_name(self):
        result = []
        for action in self.list_by_object():
            result.append(action.name)
        return result

    def list_by_object(self):
        return csaction.get(self.client)

    def get(self, action_name):
        return csaction.get(self.client, action_name)

    def delete(self, action_name):
        try:
            csaction_obj = csaction.get(self.client, action_name)
            result = csaction.delete(self.client, csaction_obj)
            self.logger.info('Action "%s" Deleted Successfully' % action_name)
        except Exception as e:
            raise e
