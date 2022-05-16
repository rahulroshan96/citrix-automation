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

class servicegroup_stats(base_resource) :
    """Statistics for service group resource."""
    def __init__(self) :
        self._servicegroupname = ""
        self._clearstats = ""
        self._state = ""
        self._servicetype = ""

    @property
    def servicegroupname(self) :
        """Name of the service group for which to display settings.<br/>Minimum length =  1."""
        try :
            return self._servicegroupname
        except Exception as e:
            raise e

    @servicegroupname.setter
    def servicegroupname(self, servicegroupname) :
        """Name of the service group for which to display settings.

        :param servicegroupname: 

        """
        try :
            self._servicegroupname = servicegroupname
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
    def servicetype(self) :
        """The service type of this service.Possible values are ADNS, DNS, MYSQL, RTSP, SSL_DIAMETER, ADNS_TCP, DNS_TCP, NNTP, SIP_UDP, SSL_TCP, ANY, FTP, RADIUS, SNMP, TCP, DHCPRA, HTTP, RDP, SSL, TFTP, DIAMETER, MSSQL, RPCSVR, SSL_BRIDGE, UDP."""
        try :
            return self._servicetype
        except Exception as e:
            raise e

    @property
    def state(self) :
        """Current state of the server. Possible values are UP, DOWN, UNKNOWN, OFS(Out of Service), TROFS(Transition Out of Service), TROFS_DOWN(Down When going Out of Service)."""
        try :
            return self._state
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(servicegroup_response, response, self.__class__.__name__.replace('_stats',''))
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.servicegroup
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.servicegroupname is not None :
                return str(self.servicegroupname)
            return None
        except Exception as e :
            raise e



    @classmethod
    def  get(cls, service, name="", option_="") :
        """Use this API to fetch the statistics of all servicegroup_stats resources that are configured on netscaler.

        :param service: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            obj = servicegroup_stats()
            if not name :
                response = obj.stat_resources(service, option_)
            else :
                obj.servicegroupname = name
                response = obj.stat_resource(service, option_)
            return response
        except Exception as e:
            raise e

    class Clearstats:
        """ """
        basic = "basic"
        full = "full"

class servicegroup_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.servicegroup = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.servicegroup = [servicegroup_stats() for _ in range(length)]

