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

class vpnvserver_vpneula_binding(base_resource) :
    """Binding class showing the vpneula that can be bound to vpnvserver."""
    def __init__(self) :
        self._eula = ""
        self._acttype = 0
        self._name = ""
        self.___count = 0

    @property
    def eula(self) :
        """Name of the EULA bound to VPN vserver."""
        try :
            return self._eula
        except Exception as e:
            raise e

    @eula.setter
    def eula(self, eula) :
        """Name of the EULA bound to VPN vserver.

        :param eula: 

        """
        try :
            self._eula = eula
        except Exception as e:
            raise e

    @property
    def name(self) :
        """Name of the virtual server.<br/>Minimum length =  1."""
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Name of the virtual server.<br/>Minimum length =  1

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def acttype(self) :
        """ """
        try :
            return self._acttype
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(vpnvserver_vpneula_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.vpnvserver_vpneula_binding
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
                updateresource = vpnvserver_vpneula_binding()
                updateresource.name = resource.name
                updateresource.eula = resource.eula
                return updateresource.update_resource(client)
            else :
                if resource and len(resource) > 0 :
                    updateresources = [vpnvserver_vpneula_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].name = resource[i].name
                        updateresources[i].eula = resource[i].eula
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
                deleteresource = vpnvserver_vpneula_binding()
                deleteresource.name = resource.name
                deleteresource.eula = resource.eula
                return deleteresource.delete_resource(client)
            else :
                if resource and len(resource) > 0 :
                    deleteresources = [vpnvserver_vpneula_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        deleteresources[i].name = resource[i].name
                        deleteresources[i].eula = resource[i].eula
                return cls.delete_bulk_request(client, deleteresources)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, service, name) :
        """Use this API to fetch vpnvserver_vpneula_binding resources.

        :param service: 
        :param name: 

        """
        try :
            obj = vpnvserver_vpneula_binding()
            obj.name = name
            response = obj.get_resources(service)
            return response
        except Exception as e:
            raise e

    @classmethod
    def get_filtered(cls, service, name, filter_) :
        """Use this API to fetch filtered set of vpnvserver_vpneula_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param name: 
        :param filter_: 

        """
        try :
            obj = vpnvserver_vpneula_binding()
            obj.name = name
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            return response
        except Exception as e:
            raise e

    @classmethod
    def count(cls, service, name) :
        """Use this API to count vpnvserver_vpneula_binding resources configued on NetScaler.

        :param service: 
        :param name: 

        """
        try :
            obj = vpnvserver_vpneula_binding()
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
        """Use this API to count the filtered set of vpnvserver_vpneula_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param name: 
        :param filter_: 

        """
        try :
            obj = vpnvserver_vpneula_binding()
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

    class Staaddresstype:
        """ """
        IPV4 = "IPV4"
        IPV6 = "IPV6"

    class Bindpoint:
        """ """
        REQUEST = "REQUEST"
        RESPONSE = "RESPONSE"
        ICA_REQUEST = "ICA_REQUEST"
        OTHERTCP_REQUEST = "OTHERTCP_REQUEST"

class vpnvserver_vpneula_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.vpnvserver_vpneula_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.vpnvserver_vpneula_binding = [vpnvserver_vpneula_binding() for _ in range(length)]

