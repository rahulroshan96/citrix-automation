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

class vpnglobal_vpnnexthopserver_binding(base_resource) :
    """Binding class showing the vpnnexthopserver that can be bound to vpnglobal."""
    def __init__(self) :
        self._nexthopserver = ""
        self.___count = 0

    @property
    def nexthopserver(self) :
        """The name of the next hop server bound to vpn global."""
        try :
            return self._nexthopserver
        except Exception as e:
            raise e

    @nexthopserver.setter
    def nexthopserver(self, nexthopserver) :
        """The name of the next hop server bound to vpn global.

        :param nexthopserver: 

        """
        try :
            self._nexthopserver = nexthopserver
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(vpnglobal_vpnnexthopserver_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.vpnglobal_vpnnexthopserver_binding
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            return 0
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
                updateresource = vpnglobal_vpnnexthopserver_binding()
                updateresource.nexthopserver = resource.nexthopserver
                return updateresource.update_resource(client)
            else :
                if resource and len(resource) > 0 :
                    updateresources = [vpnglobal_vpnnexthopserver_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].nexthopserver = resource[i].nexthopserver
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
                deleteresource = vpnglobal_vpnnexthopserver_binding()
                deleteresource.nexthopserver = resource.nexthopserver
                return deleteresource.delete_resource(client)
            else :
                if resource and len(resource) > 0 :
                    deleteresources = [vpnglobal_vpnnexthopserver_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        deleteresources[i].nexthopserver = resource[i].nexthopserver
                return cls.delete_bulk_request(client, deleteresources)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, service) :
        """Use this API to fetch a vpnglobal_vpnnexthopserver_binding resources.

        :param service: 

        """
        try :
            obj = vpnglobal_vpnnexthopserver_binding()
            response = obj.get_resources(service)
            return response
        except Exception as e:
            raise e

    @classmethod
    def get_filtered(cls, service, filter_) :
        """Use this API to fetch filtered set of vpnglobal_vpnnexthopserver_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param filter_: 

        """
        try :
            obj = vpnglobal_vpnnexthopserver_binding()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            return response
        except Exception as e:
            raise e

    @classmethod
    def count(cls, service) :
        """Use this API to count vpnglobal_vpnnexthopserver_binding resources configued on NetScaler.

        :param service: 

        """
        try :
            obj = vpnglobal_vpnnexthopserver_binding()
            option_ = options()
            option_.count = True
            response = obj.get_resources(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

    @classmethod
    def count_filtered(cls, service, filter_) :
        """Use this API to count the filtered set of vpnglobal_vpnnexthopserver_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param filter_: 

        """
        try :
            obj = vpnglobal_vpnnexthopserver_binding()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

class vpnglobal_vpnnexthopserver_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.vpnglobal_vpnnexthopserver_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.vpnglobal_vpnnexthopserver_binding = [vpnglobal_vpnnexthopserver_binding() for _ in range(length)]
