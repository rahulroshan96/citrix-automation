from .resource import Resource
import traceback
from nitro.resource.config.basic.service import service


class Service(Resource):
    def __init__(self, client, logger):
        self.client = client
        self.logger = logger

    def list_by_name(self):
        result = []
        for svc in self.list_by_object():
            result.append(svc.name)
        return result

    def list_by_object(self):
        return service.get(self.client)

    def delete(self, service_name):
        try:
            service_obj = service.get(self.client, service_name)
            result = service.delete(self.client, service_obj)
            self.logger.info('Service "%s" Deleted Successfully' % service_name)
        except Exception as e:
            self.logger.error(str(e))
            self.logger.error(traceback.print_exc())
