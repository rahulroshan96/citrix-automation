#
# Copyright (c) 2008-2015 Citrix Systems, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License")
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

from nitro.resource.base.base_resource import base_resource
from nitro.resource.base.base_resource import base_response
from nitro.service.options import options
from nitro.exception.nitro_exception import nitro_exception

from nitro.util.nitro_util import nitro_util

class lbvserver_servicegroup_binding(base_resource) :
    """Binding class showing the servicegroup that can be bound to lbvserver."""
    def __init__(self) :
        self._servicegroupname = ""
        self._servicename = ""
        self._name = ""
        self._weight = 0
        self.___count = 0

    @property
    def weight(self) :
        """Integer specifying the weight of the service. A larger number specifies a greater weight. Defines the capacity of the service relative to the other services in the load balancing configuration. Determines the priority given to the service in load balancing decisions."""
        try :
            return self._weight
        except Exception as e:
            raise e

    @weight.setter
    def weight(self, weight) :
        """Integer specifying the weight of the service. A larger number specifies a greater weight. Defines the capacity of the service relative to the other services in the load balancing configuration. Determines the priority given to the service in load balancing decisions.

        :param weight: 

        """
        try :
            self._weight = weight
        except Exception as e:
            raise e

    @property
    def name(self) :
        """Name for the virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Can be changed after the virtual server is created.
        CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my vserver" or 'my vserver'). .<br/>Minimum length =  1.


        """
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Name for the virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Can be changed after the virtual server is created.
        CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my vserver" or 'my vserver'). .<br/>Minimum length =  1

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def servicename(self) :
        """Service to bind to the virtual server.<br/>Minimum length =  1."""
        try :
            return self._servicename
        except Exception as e:
            raise e

    @servicename.setter
    def servicename(self, servicename) :
        """Service to bind to the virtual server.<br/>Minimum length =  1

        :param servicename: 

        """
        try :
            self._servicename = servicename
        except Exception as e:
            raise e

    @property
    def servicegroupname(self) :
        """The service group name bound to the selected load balancing virtual server."""
        try :
            return self._servicegroupname
        except Exception as e:
            raise e

    @servicegroupname.setter
    def servicegroupname(self, servicegroupname) :
        """The service group name bound to the selected load balancing virtual server.

        :param servicegroupname: 

        """
        try :
            self._servicegroupname = servicegroupname
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(lbvserver_servicegroup_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.lbvserver_servicegroup_binding
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.name is not None :
                return str(self.name)
            return None
        except Exception as e :
            raise e



    @classmethod
    def add(cls, client, resource) :
        """

        :param client: 
        :param resource: 

        """
        try :
            if resource and type(resource) is not list :
                updateresource = lbvserver_servicegroup_binding()
                updateresource.name = resource.name
                updateresource.servicename = resource.servicename
                updateresource.weight = resource.weight
                updateresource.servicegroupname = resource.servicegroupname
                return updateresource.update_resource(client)
            else :
                if resource and len(resource) > 0 :
                    updateresources = [lbvserver_servicegroup_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].name = resource[i].name
                        updateresources[i].servicename = resource[i].servicename
                        updateresources[i].weight = resource[i].weight
                        updateresources[i].servicegroupname = resource[i].servicegroupname
                return cls.update_bulk_request(client, updateresources)
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """

        :param client: 
        :param resource: 

        """
        try :
            if resource and type(resource) is not list :
                deleteresource = lbvserver_servicegroup_binding()
                deleteresource.name = resource.name
                deleteresource.servicename = resource.servicename
                deleteresource.servicegroupname = resource.servicegroupname
                return deleteresource.delete_resource(client)
            else :
                if resource and len(resource) > 0 :
                    deleteresources = [lbvserver_servicegroup_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        deleteresources[i].name = resource[i].name
                        deleteresources[i].servicename = resource[i].servicename
                        deleteresources[i].servicegroupname = resource[i].servicegroupname
                return cls.delete_bulk_request(client, deleteresources)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, service, name) :
        """Use this API to fetch lbvserver_servicegroup_binding resources.

        :param service: 
        :param name: 

        """
        try :
            obj = lbvserver_servicegroup_binding()
            obj.name = name
            response = obj.get_resources(service)
            return response
        except Exception as e:
            raise e

    @classmethod
    def get_filtered(cls, service, name, filter_) :
        """Use this API to fetch filtered set of lbvserver_servicegroup_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param name: 
        :param filter_: 

        """
        try :
            obj = lbvserver_servicegroup_binding()
            obj.name = name
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            return response
        except Exception as e:
            raise e

    @classmethod
    def count(cls, service, name) :
        """Use this API to count lbvserver_servicegroup_binding resources configued on NetScaler.

        :param service: 
        :param name: 

        """
        try :
            obj = lbvserver_servicegroup_binding()
            obj.name = name
            option_ = options()
            option_.count = True
            response = obj.get_resources(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

    @classmethod
    def count_filtered(cls, service, name, filter_) :
        """Use this API to count the filtered set of lbvserver_servicegroup_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param name: 
        :param filter_: 

        """
        try :
            obj = lbvserver_servicegroup_binding()
            obj.name = name
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

    class Bindpoint:
        """ """
        REQUEST = "REQUEST"
        RESPONSE = "RESPONSE"

    class Labeltype:
        """ """
        reqvserver = "reqvserver"
        resvserver = "resvserver"
        policylabel = "policylabel"

class lbvserver_servicegroup_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.lbvserver_servicegroup_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.lbvserver_servicegroup_binding = [lbvserver_servicegroup_binding() for _ in range(length)]

