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

class lbmonitor_binding(base_resource):
    """Binding class showing the resources that can be bound to lbmonitor_binding."""
    def __init__(self) :
        self._monitorname = ""
        self.lbmonitor_metric_binding = []

    @property
    def monitorname(self) :
        """Name of the monitor.<br/>Minimum length =  1."""
        try :
            return self._monitorname
        except Exception as e:
            raise e

    @monitorname.setter
    def monitorname(self, monitorname) :
        """Name of the monitor.<br/>Minimum length =  1

        :param monitorname: 

        """
        try :
            self._monitorname = monitorname
        except Exception as e:
            raise e

    @property
    def lbmonitor_metric_bindings(self) :
        """metric that can be bound to lbmonitor."""
        try :
            return self._lbmonitor_metric_binding
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(lbmonitor_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.lbmonitor_binding
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.monitorname is not None :
                return str(self.monitorname)
            return None
        except Exception as e :
            raise e



    @classmethod
    def get(self, service, monitorname) :
        """Use this API to fetch lbmonitor_binding resource.

        :param service: 
        :param monitorname: 

        """
        try :
            if type(monitorname) is not list :
                obj = lbmonitor_binding()
                obj.monitorname = monitorname
                response = obj.get_resource(service)
            else :
                if monitorname and len(monitorname) > 0 :
                    obj = [lbmonitor_binding() for _ in range(len(monitorname))]
                    for i in range(len(monitorname)) :
                        obj[i].monitorname = monitorname[i];
                        response[i] = obj[i].get_resource(service)
            return response
        except Exception as e:
            raise e

class lbmonitor_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.lbmonitor_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.lbmonitor_binding = [lbmonitor_binding() for _ in range(length)]

