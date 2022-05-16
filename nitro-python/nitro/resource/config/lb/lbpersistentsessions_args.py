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


class lbpersistentsessions_args :
    """Provides additional arguments required for fetching the lbpersistentsessions resource."""
    def __init__(self) :
        self._vserver = ""

    @property
    def vserver(self) :
        """The name of the virtual server."""
        try :
            return self._vserver
        except Exception as e:
            raise e

    @vserver.setter
    def vserver(self, vserver) :
        """The name of the virtual server.

        :param vserver: 

        """
        try :
            self._vserver = vserver
        except Exception as e:
            raise e

