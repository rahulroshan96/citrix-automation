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

class authenticationpolicy(base_resource) :
    """Configuration for Authentication Policy resource."""
    def __init__(self) :
        self._name = ""
        self._rule = ""
        self._action = ""
        self._undefaction = ""
        self._comment = ""
        self._logaction = ""
        self._newname = ""
        self._hits = 0
        self._description = ""
        self._policysubtype = ""
        self.___count = 0

    @property
    def name(self) :
        """Name for the advance AUTHENTICATION policy.
        Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after AUTHENTICATION policy is created.
        The following requirement applies only to the NetScaler CLI:
        If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication policy" or 'my authentication policy').<br/>Minimum length =  1.


        """
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Name for the advance AUTHENTICATION policy.
        Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after AUTHENTICATION policy is created.
        The following requirement applies only to the NetScaler CLI:
        If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication policy" or 'my authentication policy').<br/>Minimum length =  1

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def rule(self) :
        """Name of the NetScaler named rule, or a default syntax expression, that the policy uses to determine whether to attempt to authenticate the user with the AUTHENTICATION server."""
        try :
            return self._rule
        except Exception as e:
            raise e

    @rule.setter
    def rule(self, rule) :
        """Name of the NetScaler named rule, or a default syntax expression, that the policy uses to determine whether to attempt to authenticate the user with the AUTHENTICATION server.

        :param rule: 

        """
        try :
            self._rule = rule
        except Exception as e:
            raise e

    @property
    def action(self) :
        """Name of the authentication action to be performed if the policy matches."""
        try :
            return self._action
        except Exception as e:
            raise e

    @action.setter
    def action(self, action) :
        """Name of the authentication action to be performed if the policy matches.

        :param action: 

        """
        try :
            self._action = action
        except Exception as e:
            raise e

    @property
    def undefaction(self) :
        """Action to perform if the result of policy evaluation is undefined (UNDEF). An UNDEF event indicates an internal error condition. Only the above built-in actions can be used."""
        try :
            return self._undefaction
        except Exception as e:
            raise e

    @undefaction.setter
    def undefaction(self, undefaction) :
        """Action to perform if the result of policy evaluation is undefined (UNDEF). An UNDEF event indicates an internal error condition. Only the above built-in actions can be used.

        :param undefaction: 

        """
        try :
            self._undefaction = undefaction
        except Exception as e:
            raise e

    @property
    def comment(self) :
        """Any comments to preserve information about this policy."""
        try :
            return self._comment
        except Exception as e:
            raise e

    @comment.setter
    def comment(self, comment) :
        """Any comments to preserve information about this policy.

        :param comment: 

        """
        try :
            self._comment = comment
        except Exception as e:
            raise e

    @property
    def logaction(self) :
        """Name of messagelog action to use when a request matches this policy."""
        try :
            return self._logaction
        except Exception as e:
            raise e

    @logaction.setter
    def logaction(self, logaction) :
        """Name of messagelog action to use when a request matches this policy.

        :param logaction: 

        """
        try :
            self._logaction = logaction
        except Exception as e:
            raise e

    @property
    def newname(self) :
        """New name for the authentication policy. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters.
        The following requirement applies only to the NetScaler CLI:
        If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication policy" or 'my authentication policy').<br/>Minimum length =  1.


        """
        try :
            return self._newname
        except Exception as e:
            raise e

    @newname.setter
    def newname(self, newname) :
        """New name for the authentication policy. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters.
        The following requirement applies only to the NetScaler CLI:
        If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication policy" or 'my authentication policy').<br/>Minimum length =  1

        :param newname: 

        """
        try :
            self._newname = newname
        except Exception as e:
            raise e

    @property
    def hits(self) :
        """Number of hits."""
        try :
            return self._hits
        except Exception as e:
            raise e

    @property
    def description(self) :
        """Description of the policy."""
        try :
            return self._description
        except Exception as e:
            raise e

    @property
    def policysubtype(self) :
        """.<br/>Possible values = LOCAL, RADIUS, LDAP, TACACS, CERT, NEGOTIATE, SAML, PROFILE, DFA, SAMLIDP, WEBAUTH, OAUTH, NO_AUTHN."""
        try :
            return self._policysubtype
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(authenticationpolicy_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.authenticationpolicy
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
        """Use this API to add authenticationpolicy.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = authenticationpolicy()
                addresource.name = resource.name
                addresource.rule = resource.rule
                addresource.action = resource.action
                addresource.undefaction = resource.undefaction
                addresource.comment = resource.comment
                addresource.logaction = resource.logaction
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ authenticationpolicy() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].name = resource[i].name
                        addresources[i].rule = resource[i].rule
                        addresources[i].action = resource[i].action
                        addresources[i].undefaction = resource[i].undefaction
                        addresources[i].comment = resource[i].comment
                        addresources[i].logaction = resource[i].logaction
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete authenticationpolicy.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = authenticationpolicy()
                if type(resource) !=  type(deleteresource):
                    deleteresource.name = resource
                else :
                    deleteresource.name = resource.name
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ authenticationpolicy() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].name = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ authenticationpolicy() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].name = resource[i].name
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def update(cls, client, resource) :
        """Use this API to update authenticationpolicy.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = authenticationpolicy()
                updateresource.name = resource.name
                updateresource.rule = resource.rule
                updateresource.action = resource.action
                updateresource.undefaction = resource.undefaction
                updateresource.comment = resource.comment
                updateresource.logaction = resource.logaction
                return updateresource.update_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    updateresources = [ authenticationpolicy() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].name = resource[i].name
                        updateresources[i].rule = resource[i].rule
                        updateresources[i].action = resource[i].action
                        updateresources[i].undefaction = resource[i].undefaction
                        updateresources[i].comment = resource[i].comment
                        updateresources[i].logaction = resource[i].logaction
                result = cls.update_bulk_request(client, updateresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of authenticationpolicy resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = authenticationpolicy()
                if type(resource) !=  type(unsetresource):
                    unsetresource.name = resource
                else :
                    unsetresource.name = resource.name
                return unsetresource.unset_resource(client, args)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ authenticationpolicy() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].name = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ authenticationpolicy() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].name = resource[i].name
                result = cls.unset_bulk_request(client, unsetresources, args)
            return result
        except Exception as e :
            raise e

    @classmethod
    def rename(cls, client, resource, new_name) :
        """Use this API to rename a authenticationpolicy resource.

        :param client: 
        :param resource: 
        :param new_name: 

        """
        try :
            renameresource = authenticationpolicy()
            if type(resource) == cls :
                renameresource.name = resource.name
            else :
                renameresource.name = resource
            return renameresource.rename_resource(client,new_name)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the authenticationpolicy resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = authenticationpolicy()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = authenticationpolicy()
                        obj.name = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [authenticationpolicy() for _ in range(len(name))]
                            obj = [authenticationpolicy() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = authenticationpolicy()
                                obj[i].name = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of authenticationpolicy resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = authenticationpolicy()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the authenticationpolicy resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = authenticationpolicy()
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
        """Use this API to count filtered the set of authenticationpolicy resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = authenticationpolicy()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Policysubtype:
        """ """
        LOCAL = "LOCAL"
        RADIUS = "RADIUS"
        LDAP = "LDAP"
        TACACS = "TACACS"
        CERT = "CERT"
        NEGOTIATE = "NEGOTIATE"
        SAML = "SAML"
        PROFILE = "PROFILE"
        DFA = "DFA"
        SAMLIDP = "SAMLIDP"
        WEBAUTH = "WEBAUTH"
        OAUTH = "OAUTH"
        NO_AUTHN = "NO_AUTHN"

class authenticationpolicy_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.authenticationpolicy = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.authenticationpolicy = [authenticationpolicy() for _ in range(length)]

