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

class sslkeyfile(base_resource) :
    """Configuration for Imported ssl key files resource."""
    def __init__(self) :
        self._name = ""
        self._src = ""
        self._password = ""
        self.___count = 0

    @property
    def name(self) :
        """Name to assign to the imported key file. Must begin with an ASCII alphanumeric or underscore(_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@),equals (=), and hyphen (-) characters. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my file" or 'my file').<br/>Minimum length =  1<br/>Maximum length =  31."""
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Name to assign to the imported key file. Must begin with an ASCII alphanumeric or underscore(_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@),equals (=), and hyphen (-) characters. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my file" or 'my file').<br/>Minimum length =  1<br/>Maximum length =  31

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def src(self) :
        """URL specifying the protocol, host, and path, including file name, to the key file to be imported. For example, http://www.example.com/key_file.
        NOTE: The import fails if the object to be imported is on an HTTPS server that requires client certificate authentication for access.<br/>Minimum length =  1<br/>Maximum length =  2047.


        """
        try :
            return self._src
        except Exception as e:
            raise e

    @src.setter
    def src(self, src) :
        """URL specifying the protocol, host, and path, including file name, to the key file to be imported. For example, http://www.example.com/key_file.
        NOTE: The import fails if the object to be imported is on an HTTPS server that requires client certificate authentication for access.<br/>Minimum length =  1<br/>Maximum length =  2047

        :param src: 

        """
        try :
            self._src = src
        except Exception as e:
            raise e

    @property
    def password(self) :
        """ """
        try :
            return self._password
        except Exception as e:
            raise e

    @password.setter
    def password(self, password) :
        """

        :param password: 

        """
        try :
            self._password = password
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(sslkeyfile_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.sslkeyfile
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            return 0
        except Exception as e :
            raise e



    @classmethod
    def Import(cls, client, resource) :
        """Use this API to Import sslkeyfile.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                Importresource = sslkeyfile()
                Importresource.name = resource.name
                Importresource.src = resource.src
                Importresource.password = resource.password
                return Importresource.perform_operation(client,"Import")
            else :
                if (resource and len(resource) > 0) :
                    Importresources = [ sslkeyfile() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        Importresources[i].name = resource[i].name
                        Importresources[i].src = resource[i].src
                        Importresources[i].password = resource[i].password
                result = cls.perform_operation_bulk_request(client, Importresources,"Import")
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete sslkeyfile.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = sslkeyfile()
                deleteresource.name = resource.name
                return deleteresource.delete_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    deleteresources = [ sslkeyfile() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        deleteresources[i].name = resource[i].name
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the sslkeyfile resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = sslkeyfile()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of sslkeyfile resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = sslkeyfile()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the sslkeyfile resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = sslkeyfile()
            option_ = options()
            option_.count = True
            response = obj.get_resources(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e

    @classmethod
    def count_filtered(cls, client, filter_) :
        """Use this API to count filtered the set of sslkeyfile resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = sslkeyfile()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


class sslkeyfile_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.sslkeyfile = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.sslkeyfile = [sslkeyfile() for _ in range(length)]

