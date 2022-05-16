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

class systementitydata(base_resource) :
    """Configuration for entity data resource."""
    def __init__(self) :
        self._type = ""
        self._name = ""
        self._alldeleted = False
        self._allinactive = False
        self._datasource = ""
        self._core = 0
        self._counters = ""
        self._starttime = ""
        self._endtime = ""
        self._last = 0
        self._unit = ""
        self._response = ""
        self._startupdate = 0
        self._lastupdate = 0

    @property
    def type(self) :
        """Specify the entity type."""
        try :
            return self._type
        except Exception as e:
            raise e

    @type.setter
    def type(self, type) :
        """Specify the entity type.

        :param type: 

        """
        try :
            self._type = type
        except Exception as e:
            raise e

    @property
    def name(self) :
        """Specify the entity name."""
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Specify the entity name.

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def alldeleted(self) :
        """Specify this if you would like to delete information about all deleted entities from the database."""
        try :
            return self._alldeleted
        except Exception as e:
            raise e

    @alldeleted.setter
    def alldeleted(self, alldeleted) :
        """Specify this if you would like to delete information about all deleted entities from the database.

        :param alldeleted: 

        """
        try :
            self._alldeleted = alldeleted
        except Exception as e:
            raise e

    @property
    def allinactive(self) :
        """Specify this if you would like to delete information about all inactive entities from the database."""
        try :
            return self._allinactive
        except Exception as e:
            raise e

    @allinactive.setter
    def allinactive(self, allinactive) :
        """Specify this if you would like to delete information about all inactive entities from the database.

        :param allinactive: 

        """
        try :
            self._allinactive = allinactive
        except Exception as e:
            raise e

    @property
    def datasource(self) :
        """Specifies the source which contains all the stored counter values."""
        try :
            return self._datasource
        except Exception as e:
            raise e

    @datasource.setter
    def datasource(self, datasource) :
        """Specifies the source which contains all the stored counter values.

        :param datasource: 

        """
        try :
            self._datasource = datasource
        except Exception as e:
            raise e

    @property
    def core(self) :
        """Specify core ID of the PE in nCore."""
        try :
            return self._core
        except Exception as e:
            raise e

    @core.setter
    def core(self, core) :
        """Specify core ID of the PE in nCore.

        :param core: 

        """
        try :
            self._core = core
        except Exception as e:
            raise e

    @property
    def counters(self) :
        """Specify the counters to be collected."""
        try :
            return self._counters
        except Exception as e:
            raise e

    @counters.setter
    def counters(self, counters) :
        """Specify the counters to be collected.

        :param counters: 

        """
        try :
            self._counters = counters
        except Exception as e:
            raise e

    @property
    def starttime(self) :
        """Specify start time in mmddyyyyhhmm to start collecting values from that timestamp."""
        try :
            return self._starttime
        except Exception as e:
            raise e

    @starttime.setter
    def starttime(self, starttime) :
        """Specify start time in mmddyyyyhhmm to start collecting values from that timestamp.

        :param starttime: 

        """
        try :
            self._starttime = starttime
        except Exception as e:
            raise e

    @property
    def endtime(self) :
        """Specify end time in mmddyyyyhhmm upto which values have to be collected."""
        try :
            return self._endtime
        except Exception as e:
            raise e

    @endtime.setter
    def endtime(self, endtime) :
        """Specify end time in mmddyyyyhhmm upto which values have to be collected.

        :param endtime: 

        """
        try :
            self._endtime = endtime
        except Exception as e:
            raise e

    @property
    def last(self) :
        """Last is literal way of saying a certain time period from the current moment. Example: -last 1 hour, -last 1 day, et cetera.<br/>Default value: 1."""
        try :
            return self._last
        except Exception as e:
            raise e

    @last.setter
    def last(self, last) :
        """Last is literal way of saying a certain time period from the current moment. Example: -last 1 hour, -last 1 day, et cetera.<br/>Default value: 1

        :param last: 

        """
        try :
            self._last = last
        except Exception as e:
            raise e

    @property
    def unit(self) :
        """Specify the time period from current moment. Example 1 x where x = hours/ days/ years.<br/>Possible values = HOURS, DAYS, MONTHS."""
        try :
            return self._unit
        except Exception as e:
            raise e

    @unit.setter
    def unit(self, unit) :
        """Specify the time period from current moment. Example 1 x where x = hours/ days/ years.<br/>Possible values = HOURS, DAYS, MONTHS

        :param unit: 

        """
        try :
            self._unit = unit
        except Exception as e:
            raise e

    @property
    def response(self) :
        """ """
        try :
            return self._response
        except Exception as e:
            raise e

    @property
    def startupdate(self) :
        """ """
        try :
            return self._startupdate
        except Exception as e:
            raise e

    @property
    def lastupdate(self) :
        """ """
        try :
            return self._lastupdate
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(systementitydata_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.systementitydata
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            return 0
        except Exception as e :
            raise e



    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete systementitydata.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = systementitydata()
                deleteresource.type = resource.type
                deleteresource.name = resource.name
                deleteresource.alldeleted = resource.alldeleted
                deleteresource.allinactive = resource.allinactive
                deleteresource.datasource = resource.datasource
                deleteresource.core = resource.core
                return deleteresource.delete_resource(client)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the systementitydata resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if type(name) == cls :
                if type(name) is not list :
                    option_ = options()
                    option_.args = nitro_util.object_to_string_withoutquotes(name)
                    response = name.get_resource(client, option_)
                return response
        except Exception as e :
            raise e


    @classmethod
    def get_args(cls, client, args) :
        """Use this API to fetch all the systementitydata resources that are configured on netscaler.
            # This uses systementitydata_args which is a way to provide additional arguments while fetching the resources.

        :param client: 
        :param args: 

        """
        try :
            obj = systementitydata()
            option_ = options()
            option_.args = nitro_util.object_to_string_withoutquotes(args)
            response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    class Unit:
        """ """
        HOURS = "HOURS"
        DAYS = "DAYS"
        MONTHS = "MONTHS"

class systementitydata_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.systementitydata = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.systementitydata = [systementitydata() for _ in range(length)]

