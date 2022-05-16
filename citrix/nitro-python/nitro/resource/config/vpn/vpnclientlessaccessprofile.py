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

class vpnclientlessaccessprofile(base_resource) :
    """Configuration for Clientless VPN rewrite profile resource."""
    def __init__(self) :
        self._profilename = ""
        self._urlrewritepolicylabel = ""
        self._javascriptrewritepolicylabel = ""
        self._reqhdrrewritepolicylabel = ""
        self._reshdrrewritepolicylabel = ""
        self._regexforfindingurlinjavascript = ""
        self._regexforfindingurlincss = ""
        self._regexforfindingurlinxcomponent = ""
        self._regexforfindingurlinxml = ""
        self._regexforfindingcustomurls = ""
        self._clientconsumedcookies = ""
        self._requirepersistentcookie = ""
        self._cssrewritepolicylabel = ""
        self._xmlrewritepolicylabel = ""
        self._xcomponentrewritepolicylabel = ""
        self._isdefault = False
        self._description = ""
        self._builtin = []
        self.___count = 0

    @property
    def profilename(self) :
        """Name for the NetScaler Gateway clientless access profile. Must begin with an ASCII alphabetic or underscore (_) character, and must consist only of ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the profile is created.
        The following requirement applies only to the NetScaler CLI:
        If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my profile" or 'my profile').<br/>Minimum length =  1.


        """
        try :
            return self._profilename
        except Exception as e:
            raise e

    @profilename.setter
    def profilename(self, profilename) :
        """Name for the NetScaler Gateway clientless access profile. Must begin with an ASCII alphabetic or underscore (_) character, and must consist only of ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the profile is created.
        The following requirement applies only to the NetScaler CLI:
        If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my profile" or 'my profile').<br/>Minimum length =  1

        :param profilename: 

        """
        try :
            self._profilename = profilename
        except Exception as e:
            raise e

    @property
    def urlrewritepolicylabel(self) :
        """Name of the configured URL rewrite policy label. If you do not specify a policy label name, then URLs are not rewritten.<br/>Minimum length =  1."""
        try :
            return self._urlrewritepolicylabel
        except Exception as e:
            raise e

    @urlrewritepolicylabel.setter
    def urlrewritepolicylabel(self, urlrewritepolicylabel) :
        """Name of the configured URL rewrite policy label. If you do not specify a policy label name, then URLs are not rewritten.<br/>Minimum length =  1

        :param urlrewritepolicylabel: 

        """
        try :
            self._urlrewritepolicylabel = urlrewritepolicylabel
        except Exception as e:
            raise e

    @property
    def javascriptrewritepolicylabel(self) :
        """Name of the configured JavaScript rewrite policy label.  If you do not specify a policy label name, then JAVA scripts are not rewritten.<br/>Minimum length =  1."""
        try :
            return self._javascriptrewritepolicylabel
        except Exception as e:
            raise e

    @javascriptrewritepolicylabel.setter
    def javascriptrewritepolicylabel(self, javascriptrewritepolicylabel) :
        """Name of the configured JavaScript rewrite policy label.  If you do not specify a policy label name, then JAVA scripts are not rewritten.<br/>Minimum length =  1

        :param javascriptrewritepolicylabel: 

        """
        try :
            self._javascriptrewritepolicylabel = javascriptrewritepolicylabel
        except Exception as e:
            raise e

    @property
    def reqhdrrewritepolicylabel(self) :
        """Name of the configured Request rewrite policy label.  If you do not specify a policy label name, then requests are not rewritten.<br/>Minimum length =  1."""
        try :
            return self._reqhdrrewritepolicylabel
        except Exception as e:
            raise e

    @reqhdrrewritepolicylabel.setter
    def reqhdrrewritepolicylabel(self, reqhdrrewritepolicylabel) :
        """Name of the configured Request rewrite policy label.  If you do not specify a policy label name, then requests are not rewritten.<br/>Minimum length =  1

        :param reqhdrrewritepolicylabel: 

        """
        try :
            self._reqhdrrewritepolicylabel = reqhdrrewritepolicylabel
        except Exception as e:
            raise e

    @property
    def reshdrrewritepolicylabel(self) :
        """Name of the configured Response rewrite policy label.<br/>Minimum length =  1."""
        try :
            return self._reshdrrewritepolicylabel
        except Exception as e:
            raise e

    @reshdrrewritepolicylabel.setter
    def reshdrrewritepolicylabel(self, reshdrrewritepolicylabel) :
        """Name of the configured Response rewrite policy label.<br/>Minimum length =  1

        :param reshdrrewritepolicylabel: 

        """
        try :
            self._reshdrrewritepolicylabel = reshdrrewritepolicylabel
        except Exception as e:
            raise e

    @property
    def regexforfindingurlinjavascript(self) :
        """Name of the pattern set that contains the regular expressions, which match the URL in Java script.<br/>Minimum length =  1."""
        try :
            return self._regexforfindingurlinjavascript
        except Exception as e:
            raise e

    @regexforfindingurlinjavascript.setter
    def regexforfindingurlinjavascript(self, regexforfindingurlinjavascript) :
        """Name of the pattern set that contains the regular expressions, which match the URL in Java script.<br/>Minimum length =  1

        :param regexforfindingurlinjavascript: 

        """
        try :
            self._regexforfindingurlinjavascript = regexforfindingurlinjavascript
        except Exception as e:
            raise e

    @property
    def regexforfindingurlincss(self) :
        """Name of the pattern set that contains the regular expressions, which match the URL in the CSS.<br/>Minimum length =  1."""
        try :
            return self._regexforfindingurlincss
        except Exception as e:
            raise e

    @regexforfindingurlincss.setter
    def regexforfindingurlincss(self, regexforfindingurlincss) :
        """Name of the pattern set that contains the regular expressions, which match the URL in the CSS.<br/>Minimum length =  1

        :param regexforfindingurlincss: 

        """
        try :
            self._regexforfindingurlincss = regexforfindingurlincss
        except Exception as e:
            raise e

    @property
    def regexforfindingurlinxcomponent(self) :
        """Name of the pattern set that contains the regular expressions, which match the URL in X Component.<br/>Minimum length =  1."""
        try :
            return self._regexforfindingurlinxcomponent
        except Exception as e:
            raise e

    @regexforfindingurlinxcomponent.setter
    def regexforfindingurlinxcomponent(self, regexforfindingurlinxcomponent) :
        """Name of the pattern set that contains the regular expressions, which match the URL in X Component.<br/>Minimum length =  1

        :param regexforfindingurlinxcomponent: 

        """
        try :
            self._regexforfindingurlinxcomponent = regexforfindingurlinxcomponent
        except Exception as e:
            raise e

    @property
    def regexforfindingurlinxml(self) :
        """Name of the pattern set that contains the regular expressions, which match the URL in XML.<br/>Minimum length =  1."""
        try :
            return self._regexforfindingurlinxml
        except Exception as e:
            raise e

    @regexforfindingurlinxml.setter
    def regexforfindingurlinxml(self, regexforfindingurlinxml) :
        """Name of the pattern set that contains the regular expressions, which match the URL in XML.<br/>Minimum length =  1

        :param regexforfindingurlinxml: 

        """
        try :
            self._regexforfindingurlinxml = regexforfindingurlinxml
        except Exception as e:
            raise e

    @property
    def regexforfindingcustomurls(self) :
        """Name of the pattern set that contains the regular expressions, which match the URLs in the custom content type other than HTML, CSS, XML, XCOMP, and JavaScript. The custom content type should be included in the patset ns_cvpn_custom_content_types.<br/>Minimum length =  1."""
        try :
            return self._regexforfindingcustomurls
        except Exception as e:
            raise e

    @regexforfindingcustomurls.setter
    def regexforfindingcustomurls(self, regexforfindingcustomurls) :
        """Name of the pattern set that contains the regular expressions, which match the URLs in the custom content type other than HTML, CSS, XML, XCOMP, and JavaScript. The custom content type should be included in the patset ns_cvpn_custom_content_types.<br/>Minimum length =  1

        :param regexforfindingcustomurls: 

        """
        try :
            self._regexforfindingcustomurls = regexforfindingcustomurls
        except Exception as e:
            raise e

    @property
    def clientconsumedcookies(self) :
        """Specify the name of the pattern set containing the names of the cookies, which are allowed between the client and the server. If a pattern set is not specified, NetSCaler Gateway does not allow any cookies between the client and the server. A cookie that is not specified in the pattern set is handled by NetScaler Gateway on behalf of the client.<br/>Minimum length =  1."""
        try :
            return self._clientconsumedcookies
        except Exception as e:
            raise e

    @clientconsumedcookies.setter
    def clientconsumedcookies(self, clientconsumedcookies) :
        """Specify the name of the pattern set containing the names of the cookies, which are allowed between the client and the server. If a pattern set is not specified, NetSCaler Gateway does not allow any cookies between the client and the server. A cookie that is not specified in the pattern set is handled by NetScaler Gateway on behalf of the client.<br/>Minimum length =  1

        :param clientconsumedcookies: 

        """
        try :
            self._clientconsumedcookies = clientconsumedcookies
        except Exception as e:
            raise e

    @property
    def requirepersistentcookie(self) :
        """Specify whether a persistent session cookie is set and accepted for clientless access. If this parameter is set to ON, COM objects, such as MSOffice, which are invoked by the browser can access the files using clientless access. Use caution because the persistent cookie is stored on the disk.<br/>Default value: OFF<br/>Possible values = ON, OFF."""
        try :
            return self._requirepersistentcookie
        except Exception as e:
            raise e

    @requirepersistentcookie.setter
    def requirepersistentcookie(self, requirepersistentcookie) :
        """Specify whether a persistent session cookie is set and accepted for clientless access. If this parameter is set to ON, COM objects, such as MSOffice, which are invoked by the browser can access the files using clientless access. Use caution because the persistent cookie is stored on the disk.<br/>Default value: OFF<br/>Possible values = ON, OFF

        :param requirepersistentcookie: 

        """
        try :
            self._requirepersistentcookie = requirepersistentcookie
        except Exception as e:
            raise e

    @property
    def cssrewritepolicylabel(self) :
        """The configured CSS rewrite policylabel.<br/>Minimum length =  1."""
        try :
            return self._cssrewritepolicylabel
        except Exception as e:
            raise e

    @property
    def xmlrewritepolicylabel(self) :
        """The configured XML rewrite policylabel.<br/>Minimum length =  1."""
        try :
            return self._xmlrewritepolicylabel
        except Exception as e:
            raise e

    @property
    def xcomponentrewritepolicylabel(self) :
        """The configured X-Component rewrite policylabel.<br/>Minimum length =  1."""
        try :
            return self._xcomponentrewritepolicylabel
        except Exception as e:
            raise e

    @property
    def isdefault(self) :
        """A value of true is returned if it is a default vpnclientlessrwprofile."""
        try :
            return self._isdefault
        except Exception as e:
            raise e

    @property
    def description(self) :
        """Description of the clientless access profile."""
        try :
            return self._description
        except Exception as e:
            raise e

    @property
    def builtin(self) :
        """Flag to determine if vpn clientless rewrite profile is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL."""
        try :
            return self._builtin
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(vpnclientlessaccessprofile_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.vpnclientlessaccessprofile
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.profilename is not None :
                return str(self.profilename)
            return None
        except Exception as e :
            raise e



    @classmethod
    def add(cls, client, resource) :
        """Use this API to add vpnclientlessaccessprofile.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = vpnclientlessaccessprofile()
                addresource.profilename = resource.profilename
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ vpnclientlessaccessprofile() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].profilename = resource[i].profilename
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete vpnclientlessaccessprofile.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = vpnclientlessaccessprofile()
                if type(resource) !=  type(deleteresource):
                    deleteresource.profilename = resource
                else :
                    deleteresource.profilename = resource.profilename
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ vpnclientlessaccessprofile() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].profilename = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ vpnclientlessaccessprofile() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].profilename = resource[i].profilename
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def update(cls, client, resource) :
        """Use this API to update vpnclientlessaccessprofile.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = vpnclientlessaccessprofile()
                updateresource.profilename = resource.profilename
                updateresource.urlrewritepolicylabel = resource.urlrewritepolicylabel
                updateresource.javascriptrewritepolicylabel = resource.javascriptrewritepolicylabel
                updateresource.reqhdrrewritepolicylabel = resource.reqhdrrewritepolicylabel
                updateresource.reshdrrewritepolicylabel = resource.reshdrrewritepolicylabel
                updateresource.regexforfindingurlinjavascript = resource.regexforfindingurlinjavascript
                updateresource.regexforfindingurlincss = resource.regexforfindingurlincss
                updateresource.regexforfindingurlinxcomponent = resource.regexforfindingurlinxcomponent
                updateresource.regexforfindingurlinxml = resource.regexforfindingurlinxml
                updateresource.regexforfindingcustomurls = resource.regexforfindingcustomurls
                updateresource.clientconsumedcookies = resource.clientconsumedcookies
                updateresource.requirepersistentcookie = resource.requirepersistentcookie
                return updateresource.update_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    updateresources = [ vpnclientlessaccessprofile() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].profilename = resource[i].profilename
                        updateresources[i].urlrewritepolicylabel = resource[i].urlrewritepolicylabel
                        updateresources[i].javascriptrewritepolicylabel = resource[i].javascriptrewritepolicylabel
                        updateresources[i].reqhdrrewritepolicylabel = resource[i].reqhdrrewritepolicylabel
                        updateresources[i].reshdrrewritepolicylabel = resource[i].reshdrrewritepolicylabel
                        updateresources[i].regexforfindingurlinjavascript = resource[i].regexforfindingurlinjavascript
                        updateresources[i].regexforfindingurlincss = resource[i].regexforfindingurlincss
                        updateresources[i].regexforfindingurlinxcomponent = resource[i].regexforfindingurlinxcomponent
                        updateresources[i].regexforfindingurlinxml = resource[i].regexforfindingurlinxml
                        updateresources[i].regexforfindingcustomurls = resource[i].regexforfindingcustomurls
                        updateresources[i].clientconsumedcookies = resource[i].clientconsumedcookies
                        updateresources[i].requirepersistentcookie = resource[i].requirepersistentcookie
                result = cls.update_bulk_request(client, updateresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of vpnclientlessaccessprofile resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = vpnclientlessaccessprofile()
                if type(resource) !=  type(unsetresource):
                    unsetresource.profilename = resource
                else :
                    unsetresource.profilename = resource.profilename
                return unsetresource.unset_resource(client, args)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ vpnclientlessaccessprofile() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].profilename = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ vpnclientlessaccessprofile() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].profilename = resource[i].profilename
                result = cls.unset_bulk_request(client, unsetresources, args)
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the vpnclientlessaccessprofile resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = vpnclientlessaccessprofile()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = vpnclientlessaccessprofile()
                        obj.profilename = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [vpnclientlessaccessprofile() for _ in range(len(name))]
                            obj = [vpnclientlessaccessprofile() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = vpnclientlessaccessprofile()
                                obj[i].profilename = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of vpnclientlessaccessprofile resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = vpnclientlessaccessprofile()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the vpnclientlessaccessprofile resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = vpnclientlessaccessprofile()
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
        """Use this API to count filtered the set of vpnclientlessaccessprofile resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = vpnclientlessaccessprofile()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Builtin:
        """ """
        MODIFIABLE = "MODIFIABLE"
        DELETABLE = "DELETABLE"
        IMMUTABLE = "IMMUTABLE"
        PARTITION_ALL = "PARTITION_ALL"

    class Requirepersistentcookie:
        """ """
        ON = "ON"
        OFF = "OFF"

class vpnclientlessaccessprofile_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.vpnclientlessaccessprofile = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.vpnclientlessaccessprofile = [vpnclientlessaccessprofile() for _ in range(length)]

