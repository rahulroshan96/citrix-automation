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

class lsnclient(base_resource) :
    """Configuration for lsn client resource."""
    def __init__(self) :
        self._clientname = ""
        self._td = 0
        self.___count = 0

    @property
    def clientname(self) :
        """Name for the LSN client entity. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN client is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn client1" or 'lsn client1'). .<br/>Minimum length =  1<br/>Maximum length =  127."""
        try :
            return self._clientname
        except Exception as e:
            raise e

    @clientname.setter
    def clientname(self, clientname) :
        """Name for the LSN client entity. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN client is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn client1" or 'lsn client1'). .<br/>Minimum length =  1<br/>Maximum length =  127

        :param clientname: 

        """
        try :
            self._clientname = clientname
        except Exception as e:
            raise e

    @property
    def td(self) :
        """ID of the traffic domain on which this subscriber or the subscriber network (as specified by the network parameter) belongs.
        If you do not specify an ID, the subscriber or the subscriber network becomes part of the default traffic domain.<br/>Default value: 0<br/>Minimum value =  0<br/>Maximum value =  4094.


        """
        try :
            return self._td
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(lsnclient_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.lsnclient
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.clientname is not None :
                return str(self.clientname)
            return None
        except Exception as e :
            raise e



    @classmethod
    def add(cls, client, resource) :
        """Use this API to add lsnclient.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = lsnclient()
                addresource.clientname = resource.clientname
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ lsnclient() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].clientname = resource[i].clientname
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete lsnclient.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = lsnclient()
                if type(resource) !=  type(deleteresource):
                    deleteresource.clientname = resource
                else :
                    deleteresource.clientname = resource.clientname
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ lsnclient() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].clientname = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ lsnclient() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].clientname = resource[i].clientname
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the lsnclient resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = lsnclient()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = lsnclient()
                        obj.clientname = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [lsnclient() for _ in range(len(name))]
                            obj = [lsnclient() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = lsnclient()
                                obj[i].clientname = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of lsnclient resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = lsnclient()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the lsnclient resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = lsnclient()
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
        """Use this API to count filtered the set of lsnclient resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = lsnclient()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


class lsnclient_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.lsnclient = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.lsnclient = [lsnclient() for _ in range(length)]

