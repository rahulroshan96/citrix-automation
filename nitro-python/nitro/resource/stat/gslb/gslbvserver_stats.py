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

class gslbvserver_stats(base_resource) :
    """Statistics for Global Server Load Balancing Virtual Server resource."""
    def __init__(self) :
        self._name = ""
        self._clearstats = ""
        self._establishedconn = 0
        self._inactsvcs = 0
        self._vslbhealth = 0
        self._type = ""
        self._state = ""
        self._actsvcs = 0
        self._tothits = 0
        self._hitsrate = 0
        self._totalrequestbytes = 0
        self._requestbytesrate = 0
        self._totalresponsebytes = 0
        self._responsebytesrate = 0
        self._sothreshold = 0
        self._totspillovers = 0
        self._totvserverdownbackuphits = 0
        self._totalrequests = 0
        self._requestsrate = 0
        self._totalresponses = 0
        self._responsesrate = 0
        self._curclntconnections = 0
        self._cursrvrconnections = 0

    @property
    def name(self) :
        """Name of the GSLB virtual server for which to display statistics. If you do not specify a name, statistics are displayed for all GSLB virtual servers.<br/>Minimum length =  1."""
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Name of the GSLB virtual server for which to display statistics. If you do not specify a name, statistics are displayed for all GSLB virtual servers.

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def clearstats(self) :
        """Clear the statsistics / counters.<br/>Possible values = basic, full."""
        try :
            return self._clearstats
        except Exception as e:
            raise e

    @clearstats.setter
    def clearstats(self, clearstats) :
        """Clear the statsistics / counters

        :param clearstats: 

        """
        try :
            self._clearstats = clearstats
        except Exception as e:
            raise e

    @property
    def curclntconnections(self) :
        """Number of current client connections."""
        try :
            return self._curclntconnections
        except Exception as e:
            raise e

    @property
    def establishedconn(self) :
        """Number of client connections in ESTABLISHED state."""
        try :
            return self._establishedconn
        except Exception as e:
            raise e

    @property
    def tothits(self) :
        """Total vserver hits."""
        try :
            return self._tothits
        except Exception as e:
            raise e

    @property
    def totalrequests(self) :
        """Total number of requests received on this service or virtual server. (This applies to HTTP/SSL services and servers.)."""
        try :
            return self._totalrequests
        except Exception as e:
            raise e

    @property
    def sothreshold(self) :
        """Spill Over Threshold set on the VServer."""
        try :
            return self._sothreshold
        except Exception as e:
            raise e

    @property
    def responsebytesrate(self) :
        """Rate (/s) counter for totalresponsebytes."""
        try :
            return self._responsebytesrate
        except Exception as e:
            raise e

    @property
    def totalresponses(self) :
        """Number of responses received on this service or virtual server. (This applies to HTTP/SSL services and servers.)."""
        try :
            return self._totalresponses
        except Exception as e:
            raise e

    @property
    def requestbytesrate(self) :
        """Rate (/s) counter for totalrequestbytes."""
        try :
            return self._requestbytesrate
        except Exception as e:
            raise e

    @property
    def type(self) :
        """Protocol associated with the vserver."""
        try :
            return self._type
        except Exception as e:
            raise e

    @property
    def hitsrate(self) :
        """Rate (/s) counter for tothits."""
        try :
            return self._hitsrate
        except Exception as e:
            raise e

    @property
    def cursrvrconnections(self) :
        """Number of current connections to the actual servers behind the virtual server."""
        try :
            return self._cursrvrconnections
        except Exception as e:
            raise e

    @property
    def responsesrate(self) :
        """Rate (/s) counter for totalresponses."""
        try :
            return self._responsesrate
        except Exception as e:
            raise e

    @property
    def totspillovers(self) :
        """Number of times vserver experienced spill over."""
        try :
            return self._totspillovers
        except Exception as e:
            raise e

    @property
    def totalrequestbytes(self) :
        """Total number of request bytes received on this service or virtual server."""
        try :
            return self._totalrequestbytes
        except Exception as e:
            raise e

    @property
    def state(self) :
        """Current state of the server. Possible values are UP, DOWN, UNKNOWN, OFS(Out of Service), TROFS(Transition Out of Service), TROFS_DOWN(Down When going Out of Service)."""
        try :
            return self._state
        except Exception as e:
            raise e

    @property
    def vslbhealth(self) :
        """Health of the vserver. This gives percentage of UP services bound to this vserver."""
        try :
            return self._vslbhealth
        except Exception as e:
            raise e

    @property
    def actsvcs(self) :
        """number of ACTIVE services bound to a vserver."""
        try :
            return self._actsvcs
        except Exception as e:
            raise e

    @property
    def totalresponsebytes(self) :
        """Number of response bytes received by this service or virtual server."""
        try :
            return self._totalresponsebytes
        except Exception as e:
            raise e

    @property
    def requestsrate(self) :
        """Rate (/s) counter for totalrequests."""
        try :
            return self._requestsrate
        except Exception as e:
            raise e

    @property
    def totvserverdownbackuphits(self) :
        """Number of times traffic was diverted to backup vserver since primary vserver was DOWN."""
        try :
            return self._totvserverdownbackuphits
        except Exception as e:
            raise e

    @property
    def inactsvcs(self) :
        """number of INACTIVE services bound to a vserver."""
        try :
            return self._inactsvcs
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(gslbvserver_response, response, self.__class__.__name__.replace('_stats',''))
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.gslbvserver
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
    def  get(cls, service, name="", option_="") :
        """Use this API to fetch the statistics of all gslbvserver_stats resources that are configured on netscaler.

        :param service: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            obj = gslbvserver_stats()
            if not name :
                response = obj.stat_resources(service, option_)
            else :
                obj.name = name
                response = obj.stat_resource(service, option_)
            return response
        except Exception as e:
            raise e

    class Clearstats:
        """ """
        basic = "basic"
        full = "full"

class gslbvserver_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.gslbvserver = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.gslbvserver = [gslbvserver_stats() for _ in range(length)]

