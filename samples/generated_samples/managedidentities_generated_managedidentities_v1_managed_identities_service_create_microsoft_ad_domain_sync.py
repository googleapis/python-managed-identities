# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for CreateMicrosoftAdDomain
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-managed-identities


# [START managedidentities_generated_managedidentities_v1_ManagedIdentitiesService_CreateMicrosoftAdDomain_sync]
from google.cloud import managedidentities_v1


def sample_create_microsoft_ad_domain():
    # Create a client
    client = managedidentities_v1.ManagedIdentitiesServiceClient()

    # Initialize request argument(s)
    domain = managedidentities_v1.Domain()
    domain.name = "name_value"
    domain.reserved_ip_range = "reserved_ip_range_value"
    domain.locations = ['locations_value_1', 'locations_value_2']

    request = managedidentities_v1.CreateMicrosoftAdDomainRequest(
        parent="parent_value",
        domain_name="domain_name_value",
        domain=domain,
    )

    # Make the request
    operation = client.create_microsoft_ad_domain(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()
    print(response)

# [END managedidentities_generated_managedidentities_v1_ManagedIdentitiesService_CreateMicrosoftAdDomain_sync]