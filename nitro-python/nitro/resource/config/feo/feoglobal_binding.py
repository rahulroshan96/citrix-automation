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

class feoglobal_binding(base_resource):
    """Binding class showing the resources that can be bound to feoglobal_binding."""
    def __init__(self) :
        self.feoglobal_feopolicy_binding = []

    @property
    def feoglobal_feopolicy_bindings(self) :
        """feopolicy that can be bound to feoglobal."""
        try :
            return self._feoglobal_feopolicy_binding
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(feoglobal_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.feoglobal_binding
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            return 0
        except Exception as e :
            raise e



    @classmethod
    def get(self, service) :
        """Use this API to fetch a feoglobal_binding resource .

        :param service: 

        """
        try :
            obj = feoglobal_binding()
            response = obj.get_resource(service)
            return response

        except Exception as e:
            raise e

class feoglobal_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.feoglobal_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.feoglobal_binding = [feoglobal_binding() for _ in range(length)]

