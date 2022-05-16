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

class aaatacacsparams(base_resource) :
    """Configuration for tacacs parameters resource."""
    def __init__(self) :
        self._serverip = ""
        self._serverport = 0
        self._authtimeout = 0
        self._tacacssecret = ""
        self._authorization = ""
        self._accounting = ""
        self._auditfailedcmds = ""
        self._defaultauthenticationgroup = ""
        self._builtin = []

    @property
    def serverip(self) :
        """IP address of your TACACS+ server.<br/>Minimum length =  1."""
        try :
            return self._serverip
        except Exception as e:
            raise e

    @serverip.setter
    def serverip(self, serverip) :
        """IP address of your TACACS+ server.<br/>Minimum length =  1

        :param serverip: 

        """
        try :
            self._serverip = serverip
        except Exception as e:
            raise e

    @property
    def serverport(self) :
        """Port number on which the TACACS+ server listens for connections.<br/>Default value: 49<br/>Minimum length =  1."""
        try :
            return self._serverport
        except Exception as e:
            raise e

    @serverport.setter
    def serverport(self, serverport) :
        """Port number on which the TACACS+ server listens for connections.<br/>Default value: 49<br/>Minimum length =  1

        :param serverport: 

        """
        try :
            self._serverport = serverport
        except Exception as e:
            raise e

    @property
    def authtimeout(self) :
        """Maximum number of seconds that the NetScaler appliance waits for a response from the TACACS+ server.<br/>Default value: 3<br/>Minimum length =  1."""
        try :
            return self._authtimeout
        except Exception as e:
            raise e

    @authtimeout.setter
    def authtimeout(self, authtimeout) :
        """Maximum number of seconds that the NetScaler appliance waits for a response from the TACACS+ server.<br/>Default value: 3<br/>Minimum length =  1

        :param authtimeout: 

        """
        try :
            self._authtimeout = authtimeout
        except Exception as e:
            raise e

    @property
    def tacacssecret(self) :
        """Key shared between the TACACS+ server and clients. Required for allowing the NetScaler appliance to communicate with the TACACS+ server.<br/>Minimum length =  1."""
        try :
            return self._tacacssecret
        except Exception as e:
            raise e

    @tacacssecret.setter
    def tacacssecret(self, tacacssecret) :
        """Key shared between the TACACS+ server and clients. Required for allowing the NetScaler appliance to communicate with the TACACS+ server.<br/>Minimum length =  1

        :param tacacssecret: 

        """
        try :
            self._tacacssecret = tacacssecret
        except Exception as e:
            raise e

    @property
    def authorization(self) :
        """Use streaming authorization on the TACACS+ server.<br/>Possible values = ON, OFF."""
        try :
            return self._authorization
        except Exception as e:
            raise e

    @authorization.setter
    def authorization(self, authorization) :
        """Use streaming authorization on the TACACS+ server.<br/>Possible values = ON, OFF

        :param authorization: 

        """
        try :
            self._authorization = authorization
        except Exception as e:
            raise e

    @property
    def accounting(self) :
        """Send accounting messages to the TACACS+ server.<br/>Possible values = ON, OFF."""
        try :
            return self._accounting
        except Exception as e:
            raise e

    @accounting.setter
    def accounting(self, accounting) :
        """Send accounting messages to the TACACS+ server.<br/>Possible values = ON, OFF

        :param accounting: 

        """
        try :
            self._accounting = accounting
        except Exception as e:
            raise e

    @property
    def auditfailedcmds(self) :
        """The option for sending accounting messages to the TACACS+ server.<br/>Possible values = ON, OFF."""
        try :
            return self._auditfailedcmds
        except Exception as e:
            raise e

    @auditfailedcmds.setter
    def auditfailedcmds(self, auditfailedcmds) :
        """The option for sending accounting messages to the TACACS+ server.<br/>Possible values = ON, OFF

        :param auditfailedcmds: 

        """
        try :
            self._auditfailedcmds = auditfailedcmds
        except Exception as e:
            raise e

    @property
    def defaultauthenticationgroup(self) :
        """This is the default group that is chosen when the authentication succeeds in addition to extracted groups.<br/>Maximum length =  64."""
        try :
            return self._defaultauthenticationgroup
        except Exception as e:
            raise e

    @defaultauthenticationgroup.setter
    def defaultauthenticationgroup(self, defaultauthenticationgroup) :
        """This is the default group that is chosen when the authentication succeeds in addition to extracted groups.<br/>Maximum length =  64

        :param defaultauthenticationgroup: 

        """
        try :
            self._defaultauthenticationgroup = defaultauthenticationgroup
        except Exception as e:
            raise e

    @property
    def builtin(self) :
        """Indicates that a variable is a built-in (SYSTEM INTERNAL) type.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL."""
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
            result = service.payload_formatter.string_to_resource(aaatacacsparams_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.aaatacacsparams
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            return 0
        except Exception as e :
            raise e



    @classmethod
    def update(cls, client, resource) :
        """Use this API to update aaatacacsparams.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = aaatacacsparams()
                updateresource.serverip = resource.serverip
                updateresource.serverport = resource.serverport
                updateresource.authtimeout = resource.authtimeout
                updateresource.tacacssecret = resource.tacacssecret
                updateresource.authorization = resource.authorization
                updateresource.accounting = resource.accounting
                updateresource.auditfailedcmds = resource.auditfailedcmds
                updateresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
                return updateresource.update_resource(client)
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of aaatacacsparams resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = aaatacacsparams()
                return unsetresource.unset_resource(client, args)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the aaatacacsparams resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = aaatacacsparams()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    class Auditfailedcmds:
        """ """
        ON = "ON"
        OFF = "OFF"

    class Authorization:
        """ """
        ON = "ON"
        OFF = "OFF"

    class Builtin:
        """ """
        MODIFIABLE = "MODIFIABLE"
        DELETABLE = "DELETABLE"
        IMMUTABLE = "IMMUTABLE"
        PARTITION_ALL = "PARTITION_ALL"

    class Accounting:
        """ """
        ON = "ON"
        OFF = "OFF"

class aaatacacsparams_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.aaatacacsparams = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.aaatacacsparams = [aaatacacsparams() for _ in range(length)]

