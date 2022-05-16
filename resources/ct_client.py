import urllib3
from citrix.utils import constants
from nitro.service.nitro_service import *
from nitro.exception.nitro_exception import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_client(logger, ip_address, username, password, protocol=constants.HTTP):
    try:
        client = nitro_service(ip_address, protocol)
        if protocol and protocol == constants.HTTPS:
            client.certvalidation = False
        client.set_credential(username, password)
        client.isLogin()
        client.timeout = 3600
        return client
    except nitro_exception as e:
        logger.error("Exception::errorcode=" + str(e.errorcode) + ",message=" + e.message)
        raise e
    except Exception as e:
        logger.error("Exception::message=" + str(e.args))
        raise e
