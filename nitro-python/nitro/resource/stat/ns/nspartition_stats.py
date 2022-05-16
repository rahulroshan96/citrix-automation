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

class nspartition_stats(base_resource) :
    """Statistics for admin partition resource."""
    def __init__(self) :
        self._partitionname = ""
        self._clearstats = ""
        self._minbandwidth = 0
        self._maxbandwidth = 0
        self._maxconnection = 0
        self._maxmemory = 0
        self._currentbandwidth = 0
        self._currentconnections = 0
        self._memoryusagepcnt = 0
        self._totaldrops = 0
        self._dropsrate = 0
        self._totaltokendrops = 0
        self._tokendropsrate = 0
        self._totalconnectiondrops = 0
        self._connectiondropsrate = 0

    @property
    def partitionname(self) :
        """Name of the partition.<br/>Minimum length =  1."""
        try :
            return self._partitionname
        except Exception as e:
            raise e

    @partitionname.setter
    def partitionname(self, partitionname) :
        """Name of the partition.

        :param partitionname: 

        """
        try :
            self._partitionname = partitionname
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
    def currentconnections(self) :
        """Current Connections on this partition."""
        try :
            return self._currentconnections
        except Exception as e:
            raise e

    @property
    def tokendropsrate(self) :
        """Rate (/s) counter for totaltokendrops."""
        try :
            return self._tokendropsrate
        except Exception as e:
            raise e

    @property
    def totaltokendrops(self) :
        """Total drops(KB) for the partition."""
        try :
            return self._totaltokendrops
        except Exception as e:
            raise e

    @property
    def maxbandwidth(self) :
        """Maximum Banwidth allowed for the partition."""
        try :
            return self._maxbandwidth
        except Exception as e:
            raise e

    @property
    def minbandwidth(self) :
        """Minimum Bandwidth required by the partition."""
        try :
            return self._minbandwidth
        except Exception as e:
            raise e

    @property
    def totaldrops(self) :
        """Total packet drops for the partition."""
        try :
            return self._totaldrops
        except Exception as e:
            raise e

    @property
    def connectiondropsrate(self) :
        """Rate (/s) counter for totalconnectiondrops."""
        try :
            return self._connectiondropsrate
        except Exception as e:
            raise e

    @property
    def totalconnectiondrops(self) :
        """Total connection drops for the partition."""
        try :
            return self._totalconnectiondrops
        except Exception as e:
            raise e

    @property
    def dropsrate(self) :
        """Rate (/s) counter for totaldrops."""
        try :
            return self._dropsrate
        except Exception as e:
            raise e

    @property
    def currentbandwidth(self) :
        """Current Bandwidth usage for the partition."""
        try :
            return self._currentbandwidth
        except Exception as e:
            raise e

    @property
    def maxconnection(self) :
        """Maximum Connection allowed for the partition."""
        try :
            return self._maxconnection
        except Exception as e:
            raise e

    @property
    def maxmemory(self) :
        """Maximum memory limit for the partition."""
        try :
            return self._maxmemory
        except Exception as e:
            raise e

    @property
    def memoryusagepcnt(self) :
        """Memory usage(%) on this partition."""
        try :
            return self._memoryusagepcnt
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(nspartition_response, response, self.__class__.__name__.replace('_stats',''))
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.nspartition
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.partitionname is not None :
                return str(self.partitionname)
            return None
        except Exception as e :
            raise e



    @classmethod
    def  get(cls, service, name="", option_="") :
        """Use this API to fetch the statistics of all nspartition_stats resources that are configured on netscaler.

        :param service: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            obj = nspartition_stats()
            if not name :
                response = obj.stat_resources(service, option_)
            else :
                obj.partitionname = name
                response = obj.stat_resource(service, option_)
            return response
        except Exception as e:
            raise e

    class Clearstats:
        """ """
        basic = "basic"
        full = "full"

class nspartition_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.nspartition = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.nspartition = [nspartition_stats() for _ in range(length)]

