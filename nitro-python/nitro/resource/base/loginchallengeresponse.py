
# Copyright (c) 2008-2015 Citrix Systems, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
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

from nitro.resource.base.base_resource import base_resource 


class loginchallengeresponse(base_resource):
    """Nitro loginchallengeresponse resource class."""
    _response=""
    
    
    def loginchallengeresponse(self, response): 
        """loginchallengeresponse class constructor specifying challenge response.

        :param response: response for the security question

        """
        self._response = response
    
    def _get_object_name(self): 
        """ """
        return None
    
    
    def _get_nitro_response(self, service, response): 
        """gets the Nitro responce.

        :param service: 
        :param response: 

        """
        return None