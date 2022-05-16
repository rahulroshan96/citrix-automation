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

class ipset_nsip6_binding(base_resource) :
    """Binding class showing the nsip6 that can be bound to ipset."""
    def __init__(self) :
        self._ipaddress = ""
        self._name = ""
        self.___count = 0

    @property
    def name(self) :
        """Name of the IP set to which to bind IP addresses.<br/>Minimum length =  1."""
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Name of the IP set to which to bind IP addresses.<br/>Minimum length =  1

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def ipaddress(self) :
        """One or more IP addresses bound to the IP set.<br/>Minimum length =  1."""
        try :
            return self._ipaddress
        except Exception as e:
            raise e

    @ipaddress.setter
    def ipaddress(self, ipaddress) :
        """One or more IP addresses bound to the IP set.<br/>Minimum length =  1

        :param ipaddress: 

        """
        try :
            self._ipaddress = ipaddress
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(ipset_nsip6_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.ipset_nsip6_binding
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
                updateresource = ipset_nsip6_binding()
                updateresource.name = resource.name
                updateresource.ipaddress = resource.ipaddress
                return updateresource.update_resource(client)
            else :
                if resource and len(resource) > 0 :
                    updateresources = [ipset_nsip6_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].name = resource[i].name
                        updateresources[i].ipaddress = resource[i].ipaddress
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
                deleteresource = ipset_nsip6_binding()
                deleteresource.name = resource.name
                deleteresource.ipaddress = resource.ipaddress
                return deleteresource.delete_resource(client)
            else :
                if resource and len(resource) > 0 :
                    deleteresources = [ipset_nsip6_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        deleteresources[i].name = resource[i].name
                        deleteresources[i].ipaddress = resource[i].ipaddress
                return cls.delete_bulk_request(client, deleteresources)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, service, name) :
        """Use this API to fetch ipset_nsip6_binding resources.

        :param service: 
        :param name: 

        """
        try :
            obj = ipset_nsip6_binding()
            obj.name = name
            response = obj.get_resources(service)
            return response
        except Exception as e:
            raise e

    @classmethod
    def get_filtered(cls, service, name, filter_) :
        """Use this API to fetch filtered set of ipset_nsip6_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param name: 
        :param filter_: 

        """
        try :
            obj = ipset_nsip6_binding()
            obj.name = name
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            return response
        except Exception as e:
            raise e

    @classmethod
    def count(cls, service, name) :
        """Use this API to count ipset_nsip6_binding resources configued on NetScaler.

        :param service: 
        :param name: 

        """
        try :
            obj = ipset_nsip6_binding()
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
        """Use this API to count the filtered set of ipset_nsip6_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param name: 
        :param filter_: 

        """
        try :
            obj = ipset_nsip6_binding()
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

class ipset_nsip6_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.ipset_nsip6_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.ipset_nsip6_binding = [ipset_nsip6_binding() for _ in range(length)]

