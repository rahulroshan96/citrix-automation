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

class appqoeaction(base_resource) :
    """Configuration for AppQoS action resource."""
    def __init__(self) :
        self._name = ""
        self._priority = ""
        self._respondwith = ""
        self._customfile = ""
        self._altcontentsvcname = ""
        self._altcontentpath = ""
        self._polqdepth = 0
        self._priqdepth = 0
        self._maxconn = 0
        self._delay = 0
        self._dostrigexpression = ""
        self._dosaction = ""
        self._hits = 0
        self.___count = 0

    @property
    def name(self) :
        """Name for the AppQoE action. Must begin with a letter, number, or the underscore symbol (_). Other characters allowed, after the first character, are the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), and colon (:) characters. This is a mandatory argument."""
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Name for the AppQoE action. Must begin with a letter, number, or the underscore symbol (_). Other characters allowed, after the first character, are the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), and colon (:) characters. This is a mandatory argument.

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def priority(self) :
        """Priority for queuing the request. If server resources are not available for a request that matches the configured rule, this option specifies a priority for queuing the request until the server resources are available again. If priority is not configured then Lowest priority will be used to queue the request.<br/>Possible values = HIGH, MEDIUM, LOW, LOWEST."""
        try :
            return self._priority
        except Exception as e:
            raise e

    @priority.setter
    def priority(self, priority) :
        """Priority for queuing the request. If server resources are not available for a request that matches the configured rule, this option specifies a priority for queuing the request until the server resources are available again. If priority is not configured then Lowest priority will be used to queue the request.<br/>Possible values = HIGH, MEDIUM, LOW, LOWEST

        :param priority: 

        """
        try :
            self._priority = priority
        except Exception as e:
            raise e

    @property
    def respondwith(self) :
        """Responder action to be taken when the threshold is reached. Available settings function as follows:
        ACS - Serve content from an alternative content service
        Threshold : maxConn or delay
        NS - Serve from the NetScaler appliance (built-in response)
        Threshold : maxConn or delay.<br/>Possible values = ACS, NS.


        """
        try :
            return self._respondwith
        except Exception as e:
            raise e

    @respondwith.setter
    def respondwith(self, respondwith) :
        """Responder action to be taken when the threshold is reached. Available settings function as follows:
        ACS - Serve content from an alternative content service
        Threshold : maxConn or delay
        NS - Serve from the NetScaler appliance (built-in response)
        Threshold : maxConn or delay.<br/>Possible values = ACS, NS

        :param respondwith: 

        """
        try :
            self._respondwith = respondwith
        except Exception as e:
            raise e

    @property
    def customfile(self) :
        """name of the HTML page object to use as the response.<br/>Minimum length =  1."""
        try :
            return self._customfile
        except Exception as e:
            raise e

    @customfile.setter
    def customfile(self, customfile) :
        """name of the HTML page object to use as the response.<br/>Minimum length =  1

        :param customfile: 

        """
        try :
            self._customfile = customfile
        except Exception as e:
            raise e

    @property
    def altcontentsvcname(self) :
        """Name of the alternative content service to be used in the ACS.<br/>Minimum length =  1<br/>Maximum length =  127."""
        try :
            return self._altcontentsvcname
        except Exception as e:
            raise e

    @altcontentsvcname.setter
    def altcontentsvcname(self, altcontentsvcname) :
        """Name of the alternative content service to be used in the ACS.<br/>Minimum length =  1<br/>Maximum length =  127

        :param altcontentsvcname: 

        """
        try :
            self._altcontentsvcname = altcontentsvcname
        except Exception as e:
            raise e

    @property
    def altcontentpath(self) :
        """Path to the alternative content service to be used in the ACS.<br/>Minimum length =  4<br/>Maximum length =  127."""
        try :
            return self._altcontentpath
        except Exception as e:
            raise e

    @altcontentpath.setter
    def altcontentpath(self, altcontentpath) :
        """Path to the alternative content service to be used in the ACS.<br/>Minimum length =  4<br/>Maximum length =  127

        :param altcontentpath: 

        """
        try :
            self._altcontentpath = altcontentpath
        except Exception as e:
            raise e

    @property
    def polqdepth(self) :
        """Policy queue depth threshold value. When the policy queue size (number of requests queued for the policy binding this action is attached to) increases to the specified polqDepth value, subsequent requests are dropped to the lowest priority level.<br/>Maximum length =  0xFFFFFFFE."""
        try :
            return self._polqdepth
        except Exception as e:
            raise e

    @polqdepth.setter
    def polqdepth(self, polqdepth) :
        """Policy queue depth threshold value. When the policy queue size (number of requests queued for the policy binding this action is attached to) increases to the specified polqDepth value, subsequent requests are dropped to the lowest priority level.<br/>Maximum length =  0xFFFFFFFE

        :param polqdepth: 

        """
        try :
            self._polqdepth = polqdepth
        except Exception as e:
            raise e

    @property
    def priqdepth(self) :
        """Queue depth threshold value per priorirty level. If the queue size (number of requests in the queue of that particular priorirty) on the virtual server to which this policy is bound, increases to the specified qDepth value, subsequent requests are dropped to the lowest priority level.<br/>Maximum length =  0xFFFFFFFE."""
        try :
            return self._priqdepth
        except Exception as e:
            raise e

    @priqdepth.setter
    def priqdepth(self, priqdepth) :
        """Queue depth threshold value per priorirty level. If the queue size (number of requests in the queue of that particular priorirty) on the virtual server to which this policy is bound, increases to the specified qDepth value, subsequent requests are dropped to the lowest priority level.<br/>Maximum length =  0xFFFFFFFE

        :param priqdepth: 

        """
        try :
            self._priqdepth = priqdepth
        except Exception as e:
            raise e

    @property
    def maxconn(self) :
        """Maximum number of concurrent connections that can be open for requests that matches with rule.<br/>Minimum length =  1<br/>Maximum length =  0xFFFFFFFE."""
        try :
            return self._maxconn
        except Exception as e:
            raise e

    @maxconn.setter
    def maxconn(self, maxconn) :
        """Maximum number of concurrent connections that can be open for requests that matches with rule.<br/>Minimum length =  1<br/>Maximum length =  0xFFFFFFFE

        :param maxconn: 

        """
        try :
            self._maxconn = maxconn
        except Exception as e:
            raise e

    @property
    def delay(self) :
        """Delay threshold, in microseconds, for requests that match the policy's rule. If the delay statistics gathered for the matching request exceed the specified delay, configured action triggered for that request, if there is no action then requests are dropped to the lowest priority level.<br/>Minimum length =  1<br/>Maximum length =  599999999."""
        try :
            return self._delay
        except Exception as e:
            raise e

    @delay.setter
    def delay(self, delay) :
        """Delay threshold, in microseconds, for requests that match the policy's rule. If the delay statistics gathered for the matching request exceed the specified delay, configured action triggered for that request, if there is no action then requests are dropped to the lowest priority level.<br/>Minimum length =  1<br/>Maximum length =  599999999

        :param delay: 

        """
        try :
            self._delay = delay
        except Exception as e:
            raise e

    @property
    def dostrigexpression(self) :
        """Optional expression to add second level check to trigger DoS actions. Specifically used for Analytics based DoS response generation."""
        try :
            return self._dostrigexpression
        except Exception as e:
            raise e

    @dostrigexpression.setter
    def dostrigexpression(self, dostrigexpression) :
        """Optional expression to add second level check to trigger DoS actions. Specifically used for Analytics based DoS response generation.

        :param dostrigexpression: 

        """
        try :
            self._dostrigexpression = dostrigexpression
        except Exception as e:
            raise e

    @property
    def dosaction(self) :
        """DoS Action to take when vserver will be considered under DoS attack and corresponding rule matches. Mandatory if AppQoE actions are to be used for DoS attack prevention.<br/>Possible values = SimpleResponse, HICResponse."""
        try :
            return self._dosaction
        except Exception as e:
            raise e

    @dosaction.setter
    def dosaction(self, dosaction) :
        """DoS Action to take when vserver will be considered under DoS attack and corresponding rule matches. Mandatory if AppQoE actions are to be used for DoS attack prevention.<br/>Possible values = SimpleResponse, HICResponse

        :param dosaction: 

        """
        try :
            self._dosaction = dosaction
        except Exception as e:
            raise e

    @property
    def hits(self) :
        """ """
        try :
            return self._hits
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(appqoeaction_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.appqoeaction
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
        """Use this API to add appqoeaction.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = appqoeaction()
                addresource.name = resource.name
                addresource.priority = resource.priority
                addresource.respondwith = resource.respondwith
                addresource.customfile = resource.customfile
                addresource.altcontentsvcname = resource.altcontentsvcname
                addresource.altcontentpath = resource.altcontentpath
                addresource.polqdepth = resource.polqdepth
                addresource.priqdepth = resource.priqdepth
                addresource.maxconn = resource.maxconn
                addresource.delay = resource.delay
                addresource.dostrigexpression = resource.dostrigexpression
                addresource.dosaction = resource.dosaction
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ appqoeaction() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].name = resource[i].name
                        addresources[i].priority = resource[i].priority
                        addresources[i].respondwith = resource[i].respondwith
                        addresources[i].customfile = resource[i].customfile
                        addresources[i].altcontentsvcname = resource[i].altcontentsvcname
                        addresources[i].altcontentpath = resource[i].altcontentpath
                        addresources[i].polqdepth = resource[i].polqdepth
                        addresources[i].priqdepth = resource[i].priqdepth
                        addresources[i].maxconn = resource[i].maxconn
                        addresources[i].delay = resource[i].delay
                        addresources[i].dostrigexpression = resource[i].dostrigexpression
                        addresources[i].dosaction = resource[i].dosaction
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete appqoeaction.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = appqoeaction()
                if type(resource) !=  type(deleteresource):
                    deleteresource.name = resource
                else :
                    deleteresource.name = resource.name
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ appqoeaction() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].name = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ appqoeaction() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].name = resource[i].name
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def update(cls, client, resource) :
        """Use this API to update appqoeaction.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = appqoeaction()
                updateresource.name = resource.name
                updateresource.priority = resource.priority
                updateresource.altcontentsvcname = resource.altcontentsvcname
                updateresource.altcontentpath = resource.altcontentpath
                updateresource.polqdepth = resource.polqdepth
                updateresource.priqdepth = resource.priqdepth
                updateresource.maxconn = resource.maxconn
                updateresource.delay = resource.delay
                updateresource.dostrigexpression = resource.dostrigexpression
                updateresource.dosaction = resource.dosaction
                return updateresource.update_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    updateresources = [ appqoeaction() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].name = resource[i].name
                        updateresources[i].priority = resource[i].priority
                        updateresources[i].altcontentsvcname = resource[i].altcontentsvcname
                        updateresources[i].altcontentpath = resource[i].altcontentpath
                        updateresources[i].polqdepth = resource[i].polqdepth
                        updateresources[i].priqdepth = resource[i].priqdepth
                        updateresources[i].maxconn = resource[i].maxconn
                        updateresources[i].delay = resource[i].delay
                        updateresources[i].dostrigexpression = resource[i].dostrigexpression
                        updateresources[i].dosaction = resource[i].dosaction
                result = cls.update_bulk_request(client, updateresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of appqoeaction resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = appqoeaction()
                if type(resource) !=  type(unsetresource):
                    unsetresource.name = resource
                else :
                    unsetresource.name = resource.name
                return unsetresource.unset_resource(client, args)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ appqoeaction() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].name = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ appqoeaction() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].name = resource[i].name
                result = cls.unset_bulk_request(client, unsetresources, args)
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the appqoeaction resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = appqoeaction()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = appqoeaction()
                        obj.name = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [appqoeaction() for _ in range(len(name))]
                            obj = [appqoeaction() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = appqoeaction()
                                obj[i].name = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of appqoeaction resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = appqoeaction()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the appqoeaction resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = appqoeaction()
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
        """Use this API to count filtered the set of appqoeaction resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = appqoeaction()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Priority:
        """ """
        HIGH = "HIGH"
        MEDIUM = "MEDIUM"
        LOW = "LOW"
        LOWEST = "LOWEST"

    class Dosaction:
        """ """
        SimpleResponse = "SimpleResponse"
        HICResponse = "HICResponse"

    class Respondwith:
        """ """
        ACS = "ACS"
        NS = "NS"

class appqoeaction_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.appqoeaction = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.appqoeaction = [appqoeaction() for _ in range(length)]

