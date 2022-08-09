from .resource import Resource
import traceback
from nitro.resource.config.basic.server import server
from citrix.utils.utils import get_pagination_all

class Server(Resource):
    def __init__(self, client, logger):
        self.client = client
        self.logger = logger

    def list_by_name(self):
        result = []
        for svr in self.list_by_object():
            result.append(svr.name)
        return result

    def list_by_object(self):
        self.logger.info("Gathering Servers..Please Wait...")
        return get_pagination_all(server, self.client)

    def delete(self, server_name):
        try:
            server_obj = server.get(self.client, server_name)
            result = server.delete(self.client, server_obj)
            self.logger.info('Server "%s" Deleted Successfully' % server_name)
        except Exception as e:
            self.logger.error(str(e))
            self.logger.error(traceback.print_exc())
