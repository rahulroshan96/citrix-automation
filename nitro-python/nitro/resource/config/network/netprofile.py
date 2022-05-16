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

class netprofile(base_resource) :
    """Configuration for Network profile resource."""
    def __init__(self) :
        self._name = ""
        self._td = 0
        self._srcip = ""
        self._srcippersistency = ""
        self._overridelsn = ""
        self.___count = 0

    @property
    def name(self) :
        """Name for the net profile. Must begin with a letter, number, or the underscore character (_), and can consist of letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore characters. Cannot be changed after the profile is created. Choose a name that helps identify the net profile.<br/>Minimum length =  1."""
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Name for the net profile. Must begin with a letter, number, or the underscore character (_), and can consist of letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore characters. Cannot be changed after the profile is created. Choose a name that helps identify the net profile.<br/>Minimum length =  1

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def td(self) :
        """Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094."""
        try :
            return self._td
        except Exception as e:
            raise e

    @td.setter
    def td(self, td) :
        """Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094

        :param td: 

        """
        try :
            self._td = td
        except Exception as e:
            raise e

    @property
    def srcip(self) :
        """IP address or the name of an IP set."""
        try :
            return self._srcip
        except Exception as e:
            raise e

    @srcip.setter
    def srcip(self, srcip) :
        """IP address or the name of an IP set.

        :param srcip: 

        """
        try :
            self._srcip = srcip
        except Exception as e:
            raise e

    @property
    def srcippersistency(self) :
        """When the net profile is associated with a virtual server or its bound services, this option enables the NetScaler appliance to use the same  address, specified in the net profile, to communicate to servers for all sessions initiated from a particular client to the virtual server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._srcippersistency
        except Exception as e:
            raise e

    @srcippersistency.setter
    def srcippersistency(self, srcippersistency) :
        """When the net profile is associated with a virtual server or its bound services, this option enables the NetScaler appliance to use the same  address, specified in the net profile, to communicate to servers for all sessions initiated from a particular client to the virtual server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param srcippersistency: 

        """
        try :
            self._srcippersistency = srcippersistency
        except Exception as e:
            raise e

    @property
    def overridelsn(self) :
        """USNIP/USIP settings override LSN settings for configured
        service/virtual server traffic.. .<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.


        """
        try :
            return self._overridelsn
        except Exception as e:
            raise e

    @overridelsn.setter
    def overridelsn(self, overridelsn) :
        """USNIP/USIP settings override LSN settings for configured
        service/virtual server traffic.. .<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param overridelsn: 

        """
        try :
            self._overridelsn = overridelsn
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(netprofile_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.netprofile
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
        """Use this API to add netprofile.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = netprofile()
                addresource.name = resource.name
                addresource.td = resource.td
                addresource.srcip = resource.srcip
                addresource.srcippersistency = resource.srcippersistency
                addresource.overridelsn = resource.overridelsn
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ netprofile() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].name = resource[i].name
                        addresources[i].td = resource[i].td
                        addresources[i].srcip = resource[i].srcip
                        addresources[i].srcippersistency = resource[i].srcippersistency
                        addresources[i].overridelsn = resource[i].overridelsn
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete netprofile.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = netprofile()
                if type(resource) !=  type(deleteresource):
                    deleteresource.name = resource
                else :
                    deleteresource.name = resource.name
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ netprofile() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].name = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ netprofile() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].name = resource[i].name
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def update(cls, client, resource) :
        """Use this API to update netprofile.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = netprofile()
                updateresource.name = resource.name
                updateresource.srcip = resource.srcip
                updateresource.srcippersistency = resource.srcippersistency
                updateresource.overridelsn = resource.overridelsn
                return updateresource.update_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    updateresources = [ netprofile() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].name = resource[i].name
                        updateresources[i].srcip = resource[i].srcip
                        updateresources[i].srcippersistency = resource[i].srcippersistency
                        updateresources[i].overridelsn = resource[i].overridelsn
                result = cls.update_bulk_request(client, updateresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of netprofile resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = netprofile()
                if type(resource) !=  type(unsetresource):
                    unsetresource.name = resource
                else :
                    unsetresource.name = resource.name
                return unsetresource.unset_resource(client, args)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ netprofile() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].name = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ netprofile() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].name = resource[i].name
                result = cls.unset_bulk_request(client, unsetresources, args)
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the netprofile resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = netprofile()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = netprofile()
                        obj.name = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [netprofile() for _ in range(len(name))]
                            obj = [netprofile() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = netprofile()
                                obj[i].name = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of netprofile resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = netprofile()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the netprofile resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = netprofile()
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
        """Use this API to count filtered the set of netprofile resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = netprofile()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Srcippersistency:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Overridelsn:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

class netprofile_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.netprofile = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.netprofile = [netprofile() for _ in range(length)]

