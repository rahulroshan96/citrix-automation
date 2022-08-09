from .resource import Resource
import traceback
from nitro.resource.config.basic.servicegroup import servicegroup
from citrix.utils.utils import get_pagination_all

class ServiceGroup(Resource):
    def __init__(self, client, logger):
        self.client = client
        self.logger = logger

    def list_by_name(self):
        result = []
        for sg in self.list_by_object():
            result.append(sg._servicegroupname)
        return result

    def list_by_object(self):
        self.logger.info("Gathering ServicesGroups..Please Wait...")
        return get_pagination_all(servicegroup, self.client)

    def delete(self, sg_name):
        try:
            sg_obj = servicegroup.get(self.client, sg_name)
            result = servicegroup.delete(self.client, sg_obj)
            self.logger.info('Service Group "%s" Deleted Successfully' % sg_name)
        except Exception as e:
            self.logger.error(str(e))
            self.logger.error(traceback.print_exc())
