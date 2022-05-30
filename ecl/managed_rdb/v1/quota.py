# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from ecl.managed_rdb import mrdb_service
from ecl import resource2


class Quota(resource2.Resource):
    resource_key = "quota"
    base_path = '/quotas'
    service = mrdb_service.MrdbService()

    # Capabilities
    allow_get = True

    # Properties
    #: Max number of instances that can be created.
    max_instance_count = resource2.Body('max_instance_count', type=int)

    def show(self, session):
        resp = session.get(
            self.base_path,
            endpoint_filter=self.service,
            headers={"Accept": "application/json"}
        )
        self._translate_response(resp)
        return self