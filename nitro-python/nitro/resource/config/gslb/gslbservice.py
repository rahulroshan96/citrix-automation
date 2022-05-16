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

class gslbservice(base_resource) :
    """Configuration for GSLB service resource."""
    def __init__(self) :
        self._servicename = ""
        self._cnameentry = ""
        self._ip = ""
        self._servername = ""
        self._servicetype = ""
        self._port = 0
        self._publicip = ""
        self._publicport = 0
        self._maxclient = 0
        self._healthmonitor = ""
        self._sitename = ""
        self._state = ""
        self._cip = ""
        self._cipheader = ""
        self._sitepersistence = ""
        self._cookietimeout = 0
        self._siteprefix = ""
        self._clttimeout = 0
        self._svrtimeout = 0
        self._maxbandwidth = 0
        self._downstateflush = ""
        self._maxaaausers = 0
        self._monthreshold = 0
        self._hashid = 0
        self._comment = ""
        self._appflowlog = ""
        self._naptrreplacement = ""
        self._naptrorder = 0
        self._naptrservices = ""
        self._naptrdomainttl = 0
        self._naptrpreference = 0
        self._ipaddress = ""
        self._viewname = ""
        self._viewip = ""
        self._weight = 0
        self._monitor_name_svc = ""
        self._newname = ""
        self._gslb = ""
        self._svrstate = ""
        self._svreffgslbstate = ""
        self._gslbthreshold = 0
        self._gslbsvcstats = 0
        self._monstate = ""
        self._preferredlocation = ""
        self._monitor_state = ""
        self._statechangetimesec = ""
        self._tickssincelaststatechange = 0
        self._threshold = ""
        self._clmonowner = 0
        self._clmonview = 0
        self.___count = 0

    @property
    def servicename(self) :
        """Name for the GSLB service. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Can be changed after the GSLB service is created.
        CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my gslbsvc" or 'my gslbsvc').<br/>Minimum length =  1.


        """
        try :
            return self._servicename
        except Exception as e:
            raise e

    @servicename.setter
    def servicename(self, servicename) :
        """Name for the GSLB service. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Can be changed after the GSLB service is created.
        CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my gslbsvc" or 'my gslbsvc').<br/>Minimum length =  1

        :param servicename: 

        """
        try :
            self._servicename = servicename
        except Exception as e:
            raise e

    @property
    def cnameentry(self) :
        """Canonical name of the GSLB service. Used in CNAME-based GSLB.<br/>Minimum length =  1."""
        try :
            return self._cnameentry
        except Exception as e:
            raise e

    @cnameentry.setter
    def cnameentry(self, cnameentry) :
        """Canonical name of the GSLB service. Used in CNAME-based GSLB.<br/>Minimum length =  1

        :param cnameentry: 

        """
        try :
            self._cnameentry = cnameentry
        except Exception as e:
            raise e

    @property
    def ip(self) :
        """IP address for the GSLB service. Should represent a load balancing, content switching, or VPN virtual server on the NetScaler appliance, or the IP address of another load balancing device.<br/>Minimum length =  1."""
        try :
            return self._ip
        except Exception as e:
            raise e

    @ip.setter
    def ip(self, ip) :
        """IP address for the GSLB service. Should represent a load balancing, content switching, or VPN virtual server on the NetScaler appliance, or the IP address of another load balancing device.<br/>Minimum length =  1

        :param ip: 

        """
        try :
            self._ip = ip
        except Exception as e:
            raise e

    @property
    def servername(self) :
        """Name of the server hosting the GSLB service.<br/>Minimum length =  1."""
        try :
            return self._servername
        except Exception as e:
            raise e

    @servername.setter
    def servername(self, servername) :
        """Name of the server hosting the GSLB service.<br/>Minimum length =  1

        :param servername: 

        """
        try :
            self._servername = servername
        except Exception as e:
            raise e

    @property
    def servicetype(self) :
        """Type of service to create.<br/>Default value: NSSVC_SERVICE_UNKNOWN<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, NNTP, ANY, SIP_UDP, SIP_TCP, SIP_SSL, RADIUS, RDP, RTSP, MYSQL, MSSQL, ORACLE."""
        try :
            return self._servicetype
        except Exception as e:
            raise e

    @servicetype.setter
    def servicetype(self, servicetype) :
        """Type of service to create.<br/>Default value: NSSVC_SERVICE_UNKNOWN<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, NNTP, ANY, SIP_UDP, SIP_TCP, SIP_SSL, RADIUS, RDP, RTSP, MYSQL, MSSQL, ORACLE

        :param servicetype: 

        """
        try :
            self._servicetype = servicetype
        except Exception as e:
            raise e

    @property
    def port(self) :
        """Port on which the load balancing entity represented by this GSLB service listens.<br/>Minimum length =  1<br/>Range 1 - 65535."""
        try :
            return self._port
        except Exception as e:
            raise e

    @port.setter
    def port(self, port) :
        """Port on which the load balancing entity represented by this GSLB service listens.<br/>Minimum length =  1<br/>Range 1 - 65535

        :param port: 

        """
        try :
            self._port = port
        except Exception as e:
            raise e

    @property
    def publicip(self) :
        """The public IP address that a NAT device translates to the GSLB service's private IP address. Optional."""
        try :
            return self._publicip
        except Exception as e:
            raise e

    @publicip.setter
    def publicip(self, publicip) :
        """The public IP address that a NAT device translates to the GSLB service's private IP address. Optional.

        :param publicip: 

        """
        try :
            self._publicip = publicip
        except Exception as e:
            raise e

    @property
    def publicport(self) :
        """The public port associated with the GSLB service's public IP address. The port is mapped to the service's private port number. Applicable to the local GSLB service. Optional."""
        try :
            return self._publicport
        except Exception as e:
            raise e

    @publicport.setter
    def publicport(self, publicport) :
        """The public port associated with the GSLB service's public IP address. The port is mapped to the service's private port number. Applicable to the local GSLB service. Optional.

        :param publicport: 

        """
        try :
            self._publicport = publicport
        except Exception as e:
            raise e

    @property
    def maxclient(self) :
        """The maximum number of open connections that the service can support at any given time. A GSLB service whose connection count reaches the maximum is not considered when a GSLB decision is made, until the connection count drops below the maximum.<br/>Maximum length =  4294967294."""
        try :
            return self._maxclient
        except Exception as e:
            raise e

    @maxclient.setter
    def maxclient(self, maxclient) :
        """The maximum number of open connections that the service can support at any given time. A GSLB service whose connection count reaches the maximum is not considered when a GSLB decision is made, until the connection count drops below the maximum.<br/>Maximum length =  4294967294

        :param maxclient: 

        """
        try :
            self._maxclient = maxclient
        except Exception as e:
            raise e

    @property
    def healthmonitor(self) :
        """Monitor the health of the GSLB service.<br/>Default value: YES<br/>Possible values = YES, NO."""
        try :
            return self._healthmonitor
        except Exception as e:
            raise e

    @healthmonitor.setter
    def healthmonitor(self, healthmonitor) :
        """Monitor the health of the GSLB service.<br/>Default value: YES<br/>Possible values = YES, NO

        :param healthmonitor: 

        """
        try :
            self._healthmonitor = healthmonitor
        except Exception as e:
            raise e

    @property
    def sitename(self) :
        """Name of the GSLB site to which the service belongs.<br/>Minimum length =  1."""
        try :
            return self._sitename
        except Exception as e:
            raise e

    @sitename.setter
    def sitename(self, sitename) :
        """Name of the GSLB site to which the service belongs.<br/>Minimum length =  1

        :param sitename: 

        """
        try :
            self._sitename = sitename
        except Exception as e:
            raise e

    @property
    def state(self) :
        """Enable or disable the service.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._state
        except Exception as e:
            raise e

    @state.setter
    def state(self, state) :
        """Enable or disable the service.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED

        :param state: 

        """
        try :
            self._state = state
        except Exception as e:
            raise e

    @property
    def cip(self) :
        """In the request that is forwarded to the GSLB service, insert a header that stores the client's IP address. Client IP header insertion is used in connection-proxy based site persistence.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._cip
        except Exception as e:
            raise e

    @cip.setter
    def cip(self, cip) :
        """In the request that is forwarded to the GSLB service, insert a header that stores the client's IP address. Client IP header insertion is used in connection-proxy based site persistence.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param cip: 

        """
        try :
            self._cip = cip
        except Exception as e:
            raise e

    @property
    def cipheader(self) :
        """Name for the HTTP header that stores the client's IP address. Used with the Client IP option. If client IP header insertion is enabled on the service and a name is not specified for the header, the NetScaler appliance uses the name specified by the cipHeader parameter in the set ns param command or, in the GUI, the Client IP Header parameter in the Configure HTTP Parameters dialog box.<br/>Minimum length =  1."""
        try :
            return self._cipheader
        except Exception as e:
            raise e

    @cipheader.setter
    def cipheader(self, cipheader) :
        """Name for the HTTP header that stores the client's IP address. Used with the Client IP option. If client IP header insertion is enabled on the service and a name is not specified for the header, the NetScaler appliance uses the name specified by the cipHeader parameter in the set ns param command or, in the GUI, the Client IP Header parameter in the Configure HTTP Parameters dialog box.<br/>Minimum length =  1

        :param cipheader: 

        """
        try :
            self._cipheader = cipheader
        except Exception as e:
            raise e

    @property
    def sitepersistence(self) :
        """Use cookie-based site persistence. Applicable only to HTTP and SSL GSLB services.<br/>Possible values = ConnectionProxy, HTTPRedirect, NONE."""
        try :
            return self._sitepersistence
        except Exception as e:
            raise e

    @sitepersistence.setter
    def sitepersistence(self, sitepersistence) :
        """Use cookie-based site persistence. Applicable only to HTTP and SSL GSLB services.<br/>Possible values = ConnectionProxy, HTTPRedirect, NONE

        :param sitepersistence: 

        """
        try :
            self._sitepersistence = sitepersistence
        except Exception as e:
            raise e

    @property
    def cookietimeout(self) :
        """Timeout value, in minutes, for the cookie, when cookie based site persistence is enabled.<br/>Maximum length =  1440."""
        try :
            return self._cookietimeout
        except Exception as e:
            raise e

    @cookietimeout.setter
    def cookietimeout(self, cookietimeout) :
        """Timeout value, in minutes, for the cookie, when cookie based site persistence is enabled.<br/>Maximum length =  1440

        :param cookietimeout: 

        """
        try :
            self._cookietimeout = cookietimeout
        except Exception as e:
            raise e

    @property
    def siteprefix(self) :
        """The site's prefix string. When the service is bound to a GSLB virtual server, a GSLB site domain is generated internally for each bound service-domain pair by concatenating the site prefix of the service and the name of the domain. If the special string NONE is specified, the site-prefix string is unset. When implementing HTTP redirect site persistence, the NetScaler appliance redirects GSLB requests to GSLB services by using their site domains."""
        try :
            return self._siteprefix
        except Exception as e:
            raise e

    @siteprefix.setter
    def siteprefix(self, siteprefix) :
        """The site's prefix string. When the service is bound to a GSLB virtual server, a GSLB site domain is generated internally for each bound service-domain pair by concatenating the site prefix of the service and the name of the domain. If the special string NONE is specified, the site-prefix string is unset. When implementing HTTP redirect site persistence, the NetScaler appliance redirects GSLB requests to GSLB services by using their site domains.

        :param siteprefix: 

        """
        try :
            self._siteprefix = siteprefix
        except Exception as e:
            raise e

    @property
    def clttimeout(self) :
        """Idle time, in seconds, after which a client connection is terminated. Applicable if connection proxy based site persistence is used.<br/>Maximum length =  31536000."""
        try :
            return self._clttimeout
        except Exception as e:
            raise e

    @clttimeout.setter
    def clttimeout(self, clttimeout) :
        """Idle time, in seconds, after which a client connection is terminated. Applicable if connection proxy based site persistence is used.<br/>Maximum length =  31536000

        :param clttimeout: 

        """
        try :
            self._clttimeout = clttimeout
        except Exception as e:
            raise e

    @property
    def svrtimeout(self) :
        """Idle time, in seconds, after which a server connection is terminated. Applicable if connection proxy based site persistence is used.<br/>Maximum length =  31536000."""
        try :
            return self._svrtimeout
        except Exception as e:
            raise e

    @svrtimeout.setter
    def svrtimeout(self, svrtimeout) :
        """Idle time, in seconds, after which a server connection is terminated. Applicable if connection proxy based site persistence is used.<br/>Maximum length =  31536000

        :param svrtimeout: 

        """
        try :
            self._svrtimeout = svrtimeout
        except Exception as e:
            raise e

    @property
    def maxbandwidth(self) :
        """Integer specifying the maximum bandwidth allowed for the service. A GSLB service whose bandwidth reaches the maximum is not considered when a GSLB decision is made, until its bandwidth consumption drops below the maximum."""
        try :
            return self._maxbandwidth
        except Exception as e:
            raise e

    @maxbandwidth.setter
    def maxbandwidth(self, maxbandwidth) :
        """Integer specifying the maximum bandwidth allowed for the service. A GSLB service whose bandwidth reaches the maximum is not considered when a GSLB decision is made, until its bandwidth consumption drops below the maximum.

        :param maxbandwidth: 

        """
        try :
            self._maxbandwidth = maxbandwidth
        except Exception as e:
            raise e

    @property
    def downstateflush(self) :
        """Flush all active transactions associated with the GSLB service when its state transitions from UP to DOWN. Do not enable this option for services that must complete their transactions. Applicable if connection proxy based site persistence is used.<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._downstateflush
        except Exception as e:
            raise e

    @downstateflush.setter
    def downstateflush(self, downstateflush) :
        """Flush all active transactions associated with the GSLB service when its state transitions from UP to DOWN. Do not enable this option for services that must complete their transactions. Applicable if connection proxy based site persistence is used.<br/>Possible values = ENABLED, DISABLED

        :param downstateflush: 

        """
        try :
            self._downstateflush = downstateflush
        except Exception as e:
            raise e

    @property
    def maxaaausers(self) :
        """Maximum number of SSL VPN users that can be logged on concurrently to the VPN virtual server that is represented by this GSLB service. A GSLB service whose user count reaches the maximum is not considered when a GSLB decision is made, until the count drops below the maximum.<br/>Maximum length =  65535."""
        try :
            return self._maxaaausers
        except Exception as e:
            raise e

    @maxaaausers.setter
    def maxaaausers(self, maxaaausers) :
        """Maximum number of SSL VPN users that can be logged on concurrently to the VPN virtual server that is represented by this GSLB service. A GSLB service whose user count reaches the maximum is not considered when a GSLB decision is made, until the count drops below the maximum.<br/>Maximum length =  65535

        :param maxaaausers: 

        """
        try :
            self._maxaaausers = maxaaausers
        except Exception as e:
            raise e

    @property
    def monthreshold(self) :
        """Monitoring threshold value for the GSLB service. If the sum of the weights of the monitors that are bound to this GSLB service and are in the UP state is not equal to or greater than this threshold value, the service is marked as DOWN.<br/>Maximum length =  65535."""
        try :
            return self._monthreshold
        except Exception as e:
            raise e

    @monthreshold.setter
    def monthreshold(self, monthreshold) :
        """Monitoring threshold value for the GSLB service. If the sum of the weights of the monitors that are bound to this GSLB service and are in the UP state is not equal to or greater than this threshold value, the service is marked as DOWN.<br/>Maximum length =  65535

        :param monthreshold: 

        """
        try :
            self._monthreshold = monthreshold
        except Exception as e:
            raise e

    @property
    def hashid(self) :
        """Unique hash identifier for the GSLB service, used by hash based load balancing methods.<br/>Minimum length =  1."""
        try :
            return self._hashid
        except Exception as e:
            raise e

    @hashid.setter
    def hashid(self, hashid) :
        """Unique hash identifier for the GSLB service, used by hash based load balancing methods.<br/>Minimum length =  1

        :param hashid: 

        """
        try :
            self._hashid = hashid
        except Exception as e:
            raise e

    @property
    def comment(self) :
        """Any comments that you might want to associate with the GSLB service."""
        try :
            return self._comment
        except Exception as e:
            raise e

    @comment.setter
    def comment(self, comment) :
        """Any comments that you might want to associate with the GSLB service.

        :param comment: 

        """
        try :
            self._comment = comment
        except Exception as e:
            raise e

    @property
    def appflowlog(self) :
        """Enable logging appflow flow information.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._appflowlog
        except Exception as e:
            raise e

    @appflowlog.setter
    def appflowlog(self, appflowlog) :
        """Enable logging appflow flow information.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED

        :param appflowlog: 

        """
        try :
            self._appflowlog = appflowlog
        except Exception as e:
            raise e

    @property
    def naptrreplacement(self) :
        """The replacement domain name for this NAPTR.<br/>Maximum length =  255."""
        try :
            return self._naptrreplacement
        except Exception as e:
            raise e

    @naptrreplacement.setter
    def naptrreplacement(self, naptrreplacement) :
        """The replacement domain name for this NAPTR.<br/>Maximum length =  255

        :param naptrreplacement: 

        """
        try :
            self._naptrreplacement = naptrreplacement
        except Exception as e:
            raise e

    @property
    def naptrorder(self) :
        """An integer specifying the order in which the NAPTR records MUST be processed in order to accurately represent the ordered list of Rules. The ordering is from lowest to highest.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  65535."""
        try :
            return self._naptrorder
        except Exception as e:
            raise e

    @naptrorder.setter
    def naptrorder(self, naptrorder) :
        """An integer specifying the order in which the NAPTR records MUST be processed in order to accurately represent the ordered list of Rules. The ordering is from lowest to highest.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  65535

        :param naptrorder: 

        """
        try :
            self._naptrorder = naptrorder
        except Exception as e:
            raise e

    @property
    def naptrservices(self) :
        """Service Parameters applicable to this delegation path.<br/>Maximum length =  255."""
        try :
            return self._naptrservices
        except Exception as e:
            raise e

    @naptrservices.setter
    def naptrservices(self, naptrservices) :
        """Service Parameters applicable to this delegation path.<br/>Maximum length =  255

        :param naptrservices: 

        """
        try :
            self._naptrservices = naptrservices
        except Exception as e:
            raise e

    @property
    def naptrdomainttl(self) :
        """Modify the TTL of the internally created naptr domain.<br/>Default value: 3600<br/>Minimum length =  1."""
        try :
            return self._naptrdomainttl
        except Exception as e:
            raise e

    @naptrdomainttl.setter
    def naptrdomainttl(self, naptrdomainttl) :
        """Modify the TTL of the internally created naptr domain.<br/>Default value: 3600<br/>Minimum length =  1

        :param naptrdomainttl: 

        """
        try :
            self._naptrdomainttl = naptrdomainttl
        except Exception as e:
            raise e

    @property
    def naptrpreference(self) :
        """An integer specifying the preference of this NAPTR among NAPTR records having same order. lower the number, higher the preference.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  65535."""
        try :
            return self._naptrpreference
        except Exception as e:
            raise e

    @naptrpreference.setter
    def naptrpreference(self, naptrpreference) :
        """An integer specifying the preference of this NAPTR among NAPTR records having same order. lower the number, higher the preference.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  65535

        :param naptrpreference: 

        """
        try :
            self._naptrpreference = naptrpreference
        except Exception as e:
            raise e

    @property
    def ipaddress(self) :
        """The new IP address of the service."""
        try :
            return self._ipaddress
        except Exception as e:
            raise e

    @ipaddress.setter
    def ipaddress(self, ipaddress) :
        """The new IP address of the service.

        :param ipaddress: 

        """
        try :
            self._ipaddress = ipaddress
        except Exception as e:
            raise e

    @property
    def viewname(self) :
        """Name of the DNS view of the service. A DNS view is used in global server load balancing (GSLB) to return a predetermined IP address to a specific group of clients, which are identified by using a DNS policy.<br/>Minimum length =  1."""
        try :
            return self._viewname
        except Exception as e:
            raise e

    @viewname.setter
    def viewname(self, viewname) :
        """Name of the DNS view of the service. A DNS view is used in global server load balancing (GSLB) to return a predetermined IP address to a specific group of clients, which are identified by using a DNS policy.<br/>Minimum length =  1

        :param viewname: 

        """
        try :
            self._viewname = viewname
        except Exception as e:
            raise e

    @property
    def viewip(self) :
        """IP address to be used for the given view."""
        try :
            return self._viewip
        except Exception as e:
            raise e

    @viewip.setter
    def viewip(self, viewip) :
        """IP address to be used for the given view.

        :param viewip: 

        """
        try :
            self._viewip = viewip
        except Exception as e:
            raise e

    @property
    def weight(self) :
        """Weight to assign to the monitor-service binding. A larger number specifies a greater weight. Contributes to the monitoring threshold, which determines the state of the service.<br/>Minimum length =  1<br/>Maximum length =  100."""
        try :
            return self._weight
        except Exception as e:
            raise e

    @weight.setter
    def weight(self, weight) :
        """Weight to assign to the monitor-service binding. A larger number specifies a greater weight. Contributes to the monitoring threshold, which determines the state of the service.<br/>Minimum length =  1<br/>Maximum length =  100

        :param weight: 

        """
        try :
            self._weight = weight
        except Exception as e:
            raise e

    @property
    def monitor_name_svc(self) :
        """Name of the monitor to bind to the service.<br/>Minimum length =  1."""
        try :
            return self._monitor_name_svc
        except Exception as e:
            raise e

    @monitor_name_svc.setter
    def monitor_name_svc(self, monitor_name_svc) :
        """Name of the monitor to bind to the service.<br/>Minimum length =  1

        :param monitor_name_svc: 

        """
        try :
            self._monitor_name_svc = monitor_name_svc
        except Exception as e:
            raise e

    @property
    def newname(self) :
        """New name for the GSLB service.<br/>Minimum length =  1."""
        try :
            return self._newname
        except Exception as e:
            raise e

    @newname.setter
    def newname(self, newname) :
        """New name for the GSLB service.<br/>Minimum length =  1

        :param newname: 

        """
        try :
            self._newname = newname
        except Exception as e:
            raise e

    @property
    def gslb(self) :
        """.<br/>Default value: GSLB<br/>Possible values = REMOTE, LOCAL."""
        try :
            return self._gslb
        except Exception as e:
            raise e

    @property
    def svrstate(self) :
        """Server state.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED."""
        try :
            return self._svrstate
        except Exception as e:
            raise e

    @property
    def svreffgslbstate(self) :
        """Effective state of the gslb svc.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED."""
        try :
            return self._svreffgslbstate
        except Exception as e:
            raise e

    @property
    def gslbthreshold(self) :
        """Indicates if gslb svc has reached threshold."""
        try :
            return self._gslbthreshold
        except Exception as e:
            raise e

    @property
    def gslbsvcstats(self) :
        """Indicates if gslb svc has stats of the primary or the whole chain."""
        try :
            return self._gslbsvcstats
        except Exception as e:
            raise e

    @property
    def monstate(self) :
        """State of the monitor bound to gslb service.<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._monstate
        except Exception as e:
            raise e

    @property
    def preferredlocation(self) :
        """Prefered location."""
        try :
            return self._preferredlocation
        except Exception as e:
            raise e

    @property
    def monitor_state(self) :
        """The running state of the monitor on this service.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED."""
        try :
            return self._monitor_state
        except Exception as e:
            raise e

    @property
    def statechangetimesec(self) :
        """Time when last state change happened. Seconds part."""
        try :
            return self._statechangetimesec
        except Exception as e:
            raise e

    @property
    def tickssincelaststatechange(self) :
        """Time in 10 millisecond ticks since the last state change."""
        try :
            return self._tickssincelaststatechange
        except Exception as e:
            raise e

    @property
    def threshold(self) :
        """.<br/>Possible values = ABOVE, BELOW."""
        try :
            return self._threshold
        except Exception as e:
            raise e

    @property
    def clmonowner(self) :
        """Tells the mon owner of the gslb service.<br/>Minimum value =  0<br/>Maximum value =  32."""
        try :
            return self._clmonowner
        except Exception as e:
            raise e

    @property
    def clmonview(self) :
        """Tells the view id of the monitoring owner."""
        try :
            return self._clmonview
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(gslbservice_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.gslbservice
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.servicename is not None :
                return str(self.servicename)
            return None
        except Exception as e :
            raise e



    @classmethod
    def add(cls, client, resource) :
        """Use this API to add gslbservice.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = gslbservice()
                addresource.servicename = resource.servicename
                addresource.cnameentry = resource.cnameentry
                addresource.ip = resource.ip
                addresource.servername = resource.servername
                addresource.servicetype = resource.servicetype
                addresource.port = resource.port
                addresource.publicip = resource.publicip
                addresource.publicport = resource.publicport
                addresource.maxclient = resource.maxclient
                addresource.healthmonitor = resource.healthmonitor
                addresource.sitename = resource.sitename
                addresource.state = resource.state
                addresource.cip = resource.cip
                addresource.cipheader = resource.cipheader
                addresource.sitepersistence = resource.sitepersistence
                addresource.cookietimeout = resource.cookietimeout
                addresource.siteprefix = resource.siteprefix
                addresource.clttimeout = resource.clttimeout
                addresource.svrtimeout = resource.svrtimeout
                addresource.maxbandwidth = resource.maxbandwidth
                addresource.downstateflush = resource.downstateflush
                addresource.maxaaausers = resource.maxaaausers
                addresource.monthreshold = resource.monthreshold
                addresource.hashid = resource.hashid
                addresource.comment = resource.comment
                addresource.appflowlog = resource.appflowlog
                addresource.naptrreplacement = resource.naptrreplacement
                addresource.naptrorder = resource.naptrorder
                addresource.naptrservices = resource.naptrservices
                addresource.naptrdomainttl = resource.naptrdomainttl
                addresource.naptrpreference = resource.naptrpreference
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ gslbservice() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].servicename = resource[i].servicename
                        addresources[i].cnameentry = resource[i].cnameentry
                        addresources[i].ip = resource[i].ip
                        addresources[i].servername = resource[i].servername
                        addresources[i].servicetype = resource[i].servicetype
                        addresources[i].port = resource[i].port
                        addresources[i].publicip = resource[i].publicip
                        addresources[i].publicport = resource[i].publicport
                        addresources[i].maxclient = resource[i].maxclient
                        addresources[i].healthmonitor = resource[i].healthmonitor
                        addresources[i].sitename = resource[i].sitename
                        addresources[i].state = resource[i].state
                        addresources[i].cip = resource[i].cip
                        addresources[i].cipheader = resource[i].cipheader
                        addresources[i].sitepersistence = resource[i].sitepersistence
                        addresources[i].cookietimeout = resource[i].cookietimeout
                        addresources[i].siteprefix = resource[i].siteprefix
                        addresources[i].clttimeout = resource[i].clttimeout
                        addresources[i].svrtimeout = resource[i].svrtimeout
                        addresources[i].maxbandwidth = resource[i].maxbandwidth
                        addresources[i].downstateflush = resource[i].downstateflush
                        addresources[i].maxaaausers = resource[i].maxaaausers
                        addresources[i].monthreshold = resource[i].monthreshold
                        addresources[i].hashid = resource[i].hashid
                        addresources[i].comment = resource[i].comment
                        addresources[i].appflowlog = resource[i].appflowlog
                        addresources[i].naptrreplacement = resource[i].naptrreplacement
                        addresources[i].naptrorder = resource[i].naptrorder
                        addresources[i].naptrservices = resource[i].naptrservices
                        addresources[i].naptrdomainttl = resource[i].naptrdomainttl
                        addresources[i].naptrpreference = resource[i].naptrpreference
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete gslbservice.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = gslbservice()
                if type(resource) !=  type(deleteresource):
                    deleteresource.servicename = resource
                else :
                    deleteresource.servicename = resource.servicename
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ gslbservice() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].servicename = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ gslbservice() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].servicename = resource[i].servicename
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def update(cls, client, resource) :
        """Use this API to update gslbservice.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = gslbservice()
                updateresource.servicename = resource.servicename
                updateresource.ipaddress = resource.ipaddress
                updateresource.publicip = resource.publicip
                updateresource.publicport = resource.publicport
                updateresource.cip = resource.cip
                updateresource.cipheader = resource.cipheader
                updateresource.sitepersistence = resource.sitepersistence
                updateresource.siteprefix = resource.siteprefix
                updateresource.maxclient = resource.maxclient
                updateresource.healthmonitor = resource.healthmonitor
                updateresource.maxbandwidth = resource.maxbandwidth
                updateresource.downstateflush = resource.downstateflush
                updateresource.maxaaausers = resource.maxaaausers
                updateresource.viewname = resource.viewname
                updateresource.viewip = resource.viewip
                updateresource.monthreshold = resource.monthreshold
                updateresource.weight = resource.weight
                updateresource.monitor_name_svc = resource.monitor_name_svc
                updateresource.hashid = resource.hashid
                updateresource.comment = resource.comment
                updateresource.appflowlog = resource.appflowlog
                updateresource.naptrorder = resource.naptrorder
                updateresource.naptrpreference = resource.naptrpreference
                updateresource.naptrservices = resource.naptrservices
                updateresource.naptrreplacement = resource.naptrreplacement
                updateresource.naptrdomainttl = resource.naptrdomainttl
                return updateresource.update_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    updateresources = [ gslbservice() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].servicename = resource[i].servicename
                        updateresources[i].ipaddress = resource[i].ipaddress
                        updateresources[i].publicip = resource[i].publicip
                        updateresources[i].publicport = resource[i].publicport
                        updateresources[i].cip = resource[i].cip
                        updateresources[i].cipheader = resource[i].cipheader
                        updateresources[i].sitepersistence = resource[i].sitepersistence
                        updateresources[i].siteprefix = resource[i].siteprefix
                        updateresources[i].maxclient = resource[i].maxclient
                        updateresources[i].healthmonitor = resource[i].healthmonitor
                        updateresources[i].maxbandwidth = resource[i].maxbandwidth
                        updateresources[i].downstateflush = resource[i].downstateflush
                        updateresources[i].maxaaausers = resource[i].maxaaausers
                        updateresources[i].viewname = resource[i].viewname
                        updateresources[i].viewip = resource[i].viewip
                        updateresources[i].monthreshold = resource[i].monthreshold
                        updateresources[i].weight = resource[i].weight
                        updateresources[i].monitor_name_svc = resource[i].monitor_name_svc
                        updateresources[i].hashid = resource[i].hashid
                        updateresources[i].comment = resource[i].comment
                        updateresources[i].appflowlog = resource[i].appflowlog
                        updateresources[i].naptrorder = resource[i].naptrorder
                        updateresources[i].naptrpreference = resource[i].naptrpreference
                        updateresources[i].naptrservices = resource[i].naptrservices
                        updateresources[i].naptrreplacement = resource[i].naptrreplacement
                        updateresources[i].naptrdomainttl = resource[i].naptrdomainttl
                result = cls.update_bulk_request(client, updateresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of gslbservice resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = gslbservice()
                if type(resource) !=  type(unsetresource):
                    unsetresource.servicename = resource
                else :
                    unsetresource.servicename = resource.servicename
                return unsetresource.unset_resource(client, args)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ gslbservice() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].servicename = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ gslbservice() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].servicename = resource[i].servicename
                result = cls.unset_bulk_request(client, unsetresources, args)
            return result
        except Exception as e :
            raise e

    @classmethod
    def rename(cls, client, resource, new_servicename) :
        """Use this API to rename a gslbservice resource.

        :param client: 
        :param resource: 
        :param new_servicename: 

        """
        try :
            renameresource = gslbservice()
            if type(resource) == cls :
                renameresource.servicename = resource.servicename
            else :
                renameresource.servicename = resource
            return renameresource.rename_resource(client,new_servicename)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the gslbservice resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = gslbservice()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = gslbservice()
                        obj.servicename = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [gslbservice() for _ in range(len(name))]
                            obj = [gslbservice() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = gslbservice()
                                obj[i].servicename = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of gslbservice resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = gslbservice()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the gslbservice resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = gslbservice()
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
        """Use this API to count filtered the set of gslbservice resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = gslbservice()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class State:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Downstateflush:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Servicetype:
        """ """
        HTTP = "HTTP"
        FTP = "FTP"
        TCP = "TCP"
        UDP = "UDP"
        SSL = "SSL"
        SSL_BRIDGE = "SSL_BRIDGE"
        SSL_TCP = "SSL_TCP"
        NNTP = "NNTP"
        ANY = "ANY"
        SIP_UDP = "SIP_UDP"
        SIP_TCP = "SIP_TCP"
        SIP_SSL = "SIP_SSL"
        RADIUS = "RADIUS"
        RDP = "RDP"
        RTSP = "RTSP"
        MYSQL = "MYSQL"
        MSSQL = "MSSQL"
        ORACLE = "ORACLE"

    class Svrstate:
        """ """
        UP = "UP"
        DOWN = "DOWN"
        UNKNOWN = "UNKNOWN"
        BUSY = "BUSY"
        OUT_OF_SERVICE = "OUT OF SERVICE"
        GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
        DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
        NS_EMPTY_STR = "NS_EMPTY_STR"
        Unknown = "Unknown"
        DISABLED = "DISABLED"

    class Monitor_state:
        """ """
        UP = "UP"
        DOWN = "DOWN"
        UNKNOWN = "UNKNOWN"
        BUSY = "BUSY"
        OUT_OF_SERVICE = "OUT OF SERVICE"
        GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
        DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
        NS_EMPTY_STR = "NS_EMPTY_STR"
        Unknown = "Unknown"
        DISABLED = "DISABLED"

    class Gslb:
        """ """
        REMOTE = "REMOTE"
        LOCAL = "LOCAL"

    class Svreffgslbstate:
        """ """
        UP = "UP"
        DOWN = "DOWN"
        UNKNOWN = "UNKNOWN"
        BUSY = "BUSY"
        OUT_OF_SERVICE = "OUT OF SERVICE"
        GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
        DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
        NS_EMPTY_STR = "NS_EMPTY_STR"
        Unknown = "Unknown"
        DISABLED = "DISABLED"

    class Threshold:
        """ """
        ABOVE = "ABOVE"
        BELOW = "BELOW"

    class Cip:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Monstate:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Sitepersistence:
        """ """
        ConnectionProxy = "ConnectionProxy"
        HTTPRedirect = "HTTPRedirect"
        NONE = "NONE"

    class Healthmonitor:
        """ """
        YES = "YES"
        NO = "NO"

    class Appflowlog:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

class gslbservice_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.gslbservice = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.gslbservice = [gslbservice() for _ in range(length)]

