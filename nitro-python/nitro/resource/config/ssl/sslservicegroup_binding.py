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

class sslservicegroup_binding(base_resource):
    """Binding class showing the resources that can be bound to sslservicegroup_binding."""
    def __init__(self) :
        self._servicegroupname = ""
        self.sslservicegroup_sslcipher_binding = []
        self.sslservicegroup_ecccurve_binding = []
        self.sslservicegroup_sslcertkey_binding = []
        self.sslservicegroup_sslciphersuite_binding = []

    @property
    def servicegroupname(self) :
        """Name of the SSL service group for which to show detailed information.<br/>Minimum length =  1."""
        try :
            return self._servicegroupname
        except Exception as e:
            raise e

    @servicegroupname.setter
    def servicegroupname(self, servicegroupname) :
        """Name of the SSL service group for which to show detailed information.<br/>Minimum length =  1

        :param servicegroupname: 

        """
        try :
            self._servicegroupname = servicegroupname
        except Exception as e:
            raise e

    @property
    def sslservicegroup_sslcipher_bindings(self) :
        """sslcipher that can be bound to sslservicegroup."""
        try :
            return self._sslservicegroup_sslcipher_binding
        except Exception as e:
            raise e

    @property
    def sslservicegroup_sslciphersuite_bindings(self) :
        """sslciphersuite that can be bound to sslservicegroup."""
        try :
            return self._sslservicegroup_sslciphersuite_binding
        except Exception as e:
            raise e

    @property
    def sslservicegroup_ecccurve_bindings(self) :
        """ecccurve that can be bound to sslservicegroup."""
        try :
            return self._sslservicegroup_ecccurve_binding
        except Exception as e:
            raise e

    @property
    def sslservicegroup_sslcertkey_bindings(self) :
        """sslcertkey that can be bound to sslservicegroup."""
        try :
            return self._sslservicegroup_sslcertkey_binding
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(sslservicegroup_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.sslservicegroup_binding
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.servicegroupname is not None :
                return str(self.servicegroupname)
            return None
        except Exception as e :
            raise e



    @classmethod
    def get(self, service, servicegroupname) :
        """Use this API to fetch sslservicegroup_binding resource.

        :param service: 
        :param servicegroupname: 

        """
        try :
            if type(servicegroupname) is not list :
                obj = sslservicegroup_binding()
                obj.servicegroupname = servicegroupname
                response = obj.get_resource(service)
            else :
                if servicegroupname and len(servicegroupname) > 0 :
                    obj = [sslservicegroup_binding() for _ in range(len(servicegroupname))]
                    for i in range(len(servicegroupname)) :
                        obj[i].servicegroupname = servicegroupname[i];
                        response[i] = obj[i].get_resource(service)
            return response
        except Exception as e:
            raise e

class sslservicegroup_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.sslservicegroup_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.sslservicegroup_binding = [sslservicegroup_binding() for _ in range(length)]

