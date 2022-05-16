from .resource import Resource
from nitro.resource.config.cs.csvserver_cspolicy_binding import csvserver_cspolicy_binding
from nitro.resource.config.cs.csvserver import csvserver


class CSVServer(Resource):
    def __init__(self, client, logger):
        self.client = client
        self.logger = logger

    def list_by_name(self):
        result = []
        for server in self.list_by_object():
            result.append(server._name)
        return result

    def list_by_object(self):
        return csvserver.get(self.client)

    def delete(self, server_name):
        pass

    def delete_csvserver_cs_policy_binding(self, policy_name):
        for server in self.list_by_name():
            csvser_binding_objs = csvserver_cspolicy_binding.get(self.client, server)
            for obj in csvser_binding_objs:
                if hasattr(obj, "_policyname") and obj._policyname == policy_name:
                    if not hasattr(obj, "_bindpoint"):
                        obj.bindpoint = None
                    try:
                        csvserver_cspolicy_binding.delete(self.client, obj)
                        self.logger.info("Deleted the policy binding %s", obj._name)
                    except Exception as e:
                        pass

    def unbind_csvip_policy_delete_policy(self, vip_name):
        for csvip in self.list_by_object():
            csvip_policies_bindings = csvserver_cspolicy_binding.get(self.client, csvip._name)
            for binding in csvip_policies_bindings:
                policy_name = binding._name
                if hasattr(binding, '_targetlbvserver') and binding._targetlbvserver == vip_name:
                    if not hasattr(binding, "_bindpoint"):
                        binding.bindpoint = None
                    try:
                        csvserver_cspolicy_binding.delete(self.client, binding)
                    except:
                        pass
                    self.delete_csvserver_cs_policy_binding(policy_name)