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

class snmpcommunity(base_resource) :
    """Configuration for community resource."""
    def __init__(self) :
        self._communityname = ""
        self._permissions = ""
        self.___count = 0

    @property
    def communityname(self) :
        """The SNMP community string. Can consist of 1 to 31 characters that include uppercase and lowercase letters,numbers and special characters.
        The following requirement applies only to the NetScaler CLI:
        If the string includes one or more spaces, enclose the name in double or single quotation marks (for example, "my string" or 'my string').<br/>Minimum length =  1.


        """
        try :
            return self._communityname
        except Exception as e:
            raise e

    @communityname.setter
    def communityname(self, communityname) :
        """The SNMP community string. Can consist of 1 to 31 characters that include uppercase and lowercase letters,numbers and special characters.
        The following requirement applies only to the NetScaler CLI:
        If the string includes one or more spaces, enclose the name in double or single quotation marks (for example, "my string" or 'my string').<br/>Minimum length =  1

        :param communityname: 

        """
        try :
            self._communityname = communityname
        except Exception as e:
            raise e

    @property
    def permissions(self) :
        """The SNMP V1 or V2 query-type privilege that you want to associate with this SNMP community.<br/>Possible values = GET, GET_NEXT, GET_BULK, SET, ALL."""
        try :
            return self._permissions
        except Exception as e:
            raise e

    @permissions.setter
    def permissions(self, permissions) :
        """The SNMP V1 or V2 query-type privilege that you want to associate with this SNMP community.<br/>Possible values = GET, GET_NEXT, GET_BULK, SET, ALL

        :param permissions: 

        """
        try :
            self._permissions = permissions
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(snmpcommunity_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.snmpcommunity
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.communityname is not None :
                return str(self.communityname)
            return None
        except Exception as e :
            raise e



    @classmethod
    def add(cls, client, resource) :
        """Use this API to add snmpcommunity.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = snmpcommunity()
                addresource.communityname = resource.communityname
                addresource.permissions = resource.permissions
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ snmpcommunity() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].communityname = resource[i].communityname
                        addresources[i].permissions = resource[i].permissions
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete snmpcommunity.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = snmpcommunity()
                if type(resource) !=  type(deleteresource):
                    deleteresource.communityname = resource
                else :
                    deleteresource.communityname = resource.communityname
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ snmpcommunity() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].communityname = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ snmpcommunity() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].communityname = resource[i].communityname
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the snmpcommunity resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = snmpcommunity()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = snmpcommunity()
                        obj.communityname = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [snmpcommunity() for _ in range(len(name))]
                            obj = [snmpcommunity() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = snmpcommunity()
                                obj[i].communityname = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of snmpcommunity resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = snmpcommunity()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the snmpcommunity resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = snmpcommunity()
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
        """Use this API to count filtered the set of snmpcommunity resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = snmpcommunity()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Permissions:
        """ """
        GET = "GET"
        GET_NEXT = "GET_NEXT"
        GET_BULK = "GET_BULK"
        SET = "SET"
        ALL = "ALL"

class snmpcommunity_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.snmpcommunity = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.snmpcommunity = [snmpcommunity() for _ in range(length)]

