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

class nsacls(base_resource) :
    """Configuration for ACL entry resource."""

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(nsacls_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.nsacls
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            return 0
        except Exception as e :
            raise e



    @classmethod
    def renumber(cls, client, resource="") :
        """Use this API to renumber nsacls.

        :param client: 
        :param resource:  (Default value = "")

        """
        try :
            if type(resource) is not list :
                renumberresource = nsacls()
                return renumberresource.perform_operation(client,"renumber")
        except Exception as e :
            raise e

    @classmethod
    def clear(cls, client, resource="") :
        """Use this API to clear nsacls.

        :param client: 
        :param resource:  (Default value = "")

        """
        try :
            if type(resource) is not list :
                clearresource = nsacls()
                return clearresource.perform_operation(client,"clear")
        except Exception as e :
            raise e

    @classmethod
    def apply(cls, client, resource) :
        """Use this API to apply nsacls.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                applyresource = nsacls()
                return applyresource.perform_operation(client,"apply")
        except Exception as e :
            raise e

class nsacls_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.nsacls = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.nsacls = [nsacls() for _ in range(length)]

