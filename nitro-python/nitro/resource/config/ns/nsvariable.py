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

class nsvariable(base_resource) :
    """Configuration for variable resource."""
    def __init__(self) :
        self._name = ""
        self._type = ""
        self._scope = ""
        self._iffull = ""
        self._ifvaluetoobig = ""
        self._ifnovalue = ""
        self._init = ""
        self._expires = 0
        self._comment = ""
        self._referencecount = 0
        self.___count = 0

    @property
    def name(self) :
        """Variable name.  This follows the same syntax rules as other default syntax expression entity names:
        It must begin with an alpha character (A-Z or a-z) or an underscore (_).
        The rest of the characters must be alpha, numeric (0-9) or underscores.
        It cannot be re or xp (reserved for regular and XPath expressions).
        It cannot be a default syntax expression reserved word (e.g. SYS or HTTP).
        It cannot be used for an existing default syntax expression object (HTTP callout, patset, dataset, stringmap, or named expression).<br/>Minimum length =  1.


        """
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Variable name.  This follows the same syntax rules as other default syntax expression entity names:
        It must begin with an alpha character (A-Z or a-z) or an underscore (_).
        The rest of the characters must be alpha, numeric (0-9) or underscores.
        It cannot be re or xp (reserved for regular and XPath expressions).
        It cannot be a default syntax expression reserved word (e.g. SYS or HTTP).
        It cannot be used for an existing default syntax expression object (HTTP callout, patset, dataset, stringmap, or named expression).<br/>Minimum length =  1

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def type(self) :
        """Specification of the variable type; one of the following:
        ulong - singleton variable with an unsigned 64-bit value.
        text(value-max-size) - singleton variable with a text string value.
        map(text(key-max-size),ulong,max-entries) - map of text string keys to unsigned 64-bit values.
        map(text(key-max-size),text(value-max-size),max-entries) - map of text string keys to text string values.
        where
        value-max-size is a positive integer that is the maximum number of bytes in a text string value.
        key-max-size is a positive integer that is the maximum number of bytes in a text string key.
        max-entries is a positive integer that is the maximum number of entries in a map variable.
        For a global singleton text variable, value-max-size <= 64000.
        For a global map with ulong values, key-max-size <= 64000.
        For a global map with text values,  key-max-size + value-max-size <= 64000.
        max-entries is a positive integer that is the maximum number of entries in a map variable. This has a theoretical maximum of 2^64-1, but in actual use will be much smaller, considering the memory available for use by the map.
        Example:
        map(text(10),text(20),100) specifies a map of text string keys (max size 10 bytes) to text string values (max size 20 bytes), with 100 max entries.<br/>Minimum length =  1.


        """
        try :
            return self._type
        except Exception as e:
            raise e

    @type.setter
    def type(self, type) :
        """Specification of the variable type; one of the following:
        ulong - singleton variable with an unsigned 64-bit value.
        text(value-max-size) - singleton variable with a text string value.
        map(text(key-max-size),ulong,max-entries) - map of text string keys to unsigned 64-bit values.
        map(text(key-max-size),text(value-max-size),max-entries) - map of text string keys to text string values.
        where
        value-max-size is a positive integer that is the maximum number of bytes in a text string value.
        key-max-size is a positive integer that is the maximum number of bytes in a text string key.
        max-entries is a positive integer that is the maximum number of entries in a map variable.
        For a global singleton text variable, value-max-size <= 64000.
        For a global map with ulong values, key-max-size <= 64000.
        For a global map with text values,  key-max-size + value-max-size <= 64000.
        max-entries is a positive integer that is the maximum number of entries in a map variable. This has a theoretical maximum of 2^64-1, but in actual use will be much smaller, considering the memory available for use by the map.
        Example:
        map(text(10),text(20),100) specifies a map of text string keys (max size 10 bytes) to text string values (max size 20 bytes), with 100 max entries.<br/>Minimum length =  1

        :param type: 

        """
        try :
            self._type = type
        except Exception as e:
            raise e

    @property
    def scope(self) :
        """Scope of the variable:
        global - (default) one set of values visible across all Packet Engines and, in a cluster, all nodes
        transaction - one value for each request-response transaction (singleton variables only; no expiration).<br/>Default value: global<br/>Possible values = global, transaction.


        """
        try :
            return self._scope
        except Exception as e:
            raise e

    @scope.setter
    def scope(self, scope) :
        """Scope of the variable:
        global - (default) one set of values visible across all Packet Engines and, in a cluster, all nodes
        transaction - one value for each request-response transaction (singleton variables only; no expiration).<br/>Default value: global<br/>Possible values = global, transaction

        :param scope: 

        """
        try :
            self._scope = scope
        except Exception as e:
            raise e

    @property
    def iffull(self) :
        """Action to perform if an assignment to a map exceeds its configured max-entries:
        lru - (default) reuse the least recently used entry in the map.
        undef - force the assignment to return an undefined (Undef) result to the policy executing the assignment.<br/>Default value: lru<br/>Possible values = undef, lru.


        """
        try :
            return self._iffull
        except Exception as e:
            raise e

    @iffull.setter
    def iffull(self, iffull) :
        """Action to perform if an assignment to a map exceeds its configured max-entries:
        lru - (default) reuse the least recently used entry in the map.
        undef - force the assignment to return an undefined (Undef) result to the policy executing the assignment.<br/>Default value: lru<br/>Possible values = undef, lru

        :param iffull: 

        """
        try :
            self._iffull = iffull
        except Exception as e:
            raise e

    @property
    def ifvaluetoobig(self) :
        """Action to perform if an value is assigned to a text variable that exceeds its configured max-size,
        or if a key is used that exceeds its configured max-size:
        truncate - (default) truncate the text string to the first max-size bytes and proceed.
        undef - force the assignment or expression evaluation to return an undefined (Undef) result to the policy executing the assignment or expression.<br/>Default value: truncate<br/>Possible values = undef, truncate.


        """
        try :
            return self._ifvaluetoobig
        except Exception as e:
            raise e

    @ifvaluetoobig.setter
    def ifvaluetoobig(self, ifvaluetoobig) :
        """Action to perform if an value is assigned to a text variable that exceeds its configured max-size,
        or if a key is used that exceeds its configured max-size:
        truncate - (default) truncate the text string to the first max-size bytes and proceed.
        undef - force the assignment or expression evaluation to return an undefined (Undef) result to the policy executing the assignment or expression.<br/>Default value: truncate<br/>Possible values = undef, truncate

        :param ifvaluetoobig: 

        """
        try :
            self._ifvaluetoobig = ifvaluetoobig
        except Exception as e:
            raise e

    @property
    def ifnovalue(self) :
        """Action to perform if on a variable reference in an expression if the variable is single-valued and uninitialized
        or if the variable is a map and there is no value for the specified key:
        init - (default) initialize the single-value variable, or create a map entry for the key and the initial value,
        using the -init value or its default.
        undef - force the expression evaluation to return an undefined (Undef) result to the policy executing the expression.<br/>Default value: init<br/>Possible values = undef, init.


        """
        try :
            return self._ifnovalue
        except Exception as e:
            raise e

    @ifnovalue.setter
    def ifnovalue(self, ifnovalue) :
        """Action to perform if on a variable reference in an expression if the variable is single-valued and uninitialized
        or if the variable is a map and there is no value for the specified key:
        init - (default) initialize the single-value variable, or create a map entry for the key and the initial value,
        using the -init value or its default.
        undef - force the expression evaluation to return an undefined (Undef) result to the policy executing the expression.<br/>Default value: init<br/>Possible values = undef, init

        :param ifnovalue: 

        """
        try :
            self._ifnovalue = ifnovalue
        except Exception as e:
            raise e

    @property
    def init(self) :
        """Initialization value for values in this variable. Default: 0 for ulong, NULL for text."""
        try :
            return self._init
        except Exception as e:
            raise e

    @init.setter
    def init(self, init) :
        """Initialization value for values in this variable. Default: 0 for ulong, NULL for text.

        :param init: 

        """
        try :
            self._init = init
        except Exception as e:
            raise e

    @property
    def expires(self) :
        """Value expiration in seconds. If the value is not referenced within the expiration period it will be deleted. 0 (the default) means no expiration.<br/>Maximum length =  31622400."""
        try :
            return self._expires
        except Exception as e:
            raise e

    @expires.setter
    def expires(self, expires) :
        """Value expiration in seconds. If the value is not referenced within the expiration period it will be deleted. 0 (the default) means no expiration.<br/>Maximum length =  31622400

        :param expires: 

        """
        try :
            self._expires = expires
        except Exception as e:
            raise e

    @property
    def comment(self) :
        """Comments associated with this variable."""
        try :
            return self._comment
        except Exception as e:
            raise e

    @comment.setter
    def comment(self, comment) :
        """Comments associated with this variable.

        :param comment: 

        """
        try :
            self._comment = comment
        except Exception as e:
            raise e

    @property
    def referencecount(self) :
        """The number of references to the variable in expressions and assignments."""
        try :
            return self._referencecount
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(nsvariable_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.nsvariable
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
        """Use this API to add nsvariable.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = nsvariable()
                addresource.name = resource.name
                addresource.type = resource.type
                addresource.scope = resource.scope
                addresource.iffull = resource.iffull
                addresource.ifvaluetoobig = resource.ifvaluetoobig
                addresource.ifnovalue = resource.ifnovalue
                addresource.init = resource.init
                addresource.expires = resource.expires
                addresource.comment = resource.comment
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ nsvariable() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].name = resource[i].name
                        addresources[i].type = resource[i].type
                        addresources[i].scope = resource[i].scope
                        addresources[i].iffull = resource[i].iffull
                        addresources[i].ifvaluetoobig = resource[i].ifvaluetoobig
                        addresources[i].ifnovalue = resource[i].ifnovalue
                        addresources[i].init = resource[i].init
                        addresources[i].expires = resource[i].expires
                        addresources[i].comment = resource[i].comment
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def update(cls, client, resource) :
        """Use this API to update nsvariable.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = nsvariable()
                updateresource.name = resource.name
                updateresource.type = resource.type
                updateresource.iffull = resource.iffull
                updateresource.ifvaluetoobig = resource.ifvaluetoobig
                updateresource.ifnovalue = resource.ifnovalue
                updateresource.init = resource.init
                updateresource.expires = resource.expires
                updateresource.comment = resource.comment
                return updateresource.update_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    updateresources = [ nsvariable() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].name = resource[i].name
                        updateresources[i].type = resource[i].type
                        updateresources[i].iffull = resource[i].iffull
                        updateresources[i].ifvaluetoobig = resource[i].ifvaluetoobig
                        updateresources[i].ifnovalue = resource[i].ifnovalue
                        updateresources[i].init = resource[i].init
                        updateresources[i].expires = resource[i].expires
                        updateresources[i].comment = resource[i].comment
                result = cls.update_bulk_request(client, updateresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of nsvariable resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = nsvariable()
                if type(resource) !=  type(unsetresource):
                    unsetresource.name = resource
                else :
                    unsetresource.name = resource.name
                return unsetresource.unset_resource(client, args)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ nsvariable() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].name = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ nsvariable() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].name = resource[i].name
                result = cls.unset_bulk_request(client, unsetresources, args)
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete nsvariable.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = nsvariable()
                if type(resource) !=  type(deleteresource):
                    deleteresource.name = resource
                else :
                    deleteresource.name = resource.name
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ nsvariable() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].name = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ nsvariable() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].name = resource[i].name
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the nsvariable resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = nsvariable()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = nsvariable()
                        obj.name = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [nsvariable() for _ in range(len(name))]
                            obj = [nsvariable() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = nsvariable()
                                obj[i].name = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of nsvariable resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = nsvariable()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the nsvariable resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = nsvariable()
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
        """Use this API to count filtered the set of nsvariable resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = nsvariable()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Iffull:
        """ """
        undef = "undef"
        lru = "lru"

    class Scope:
        """ """
        GLOBAL = "global"
        transaction = "transaction"

    class Ifvaluetoobig:
        """ """
        undef = "undef"
        truncate = "truncate"

    class Ifnovalue:
        """ """
        undef = "undef"
        init = "init"

class nsvariable_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.nsvariable = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.nsvariable = [nsvariable() for _ in range(length)]

