#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""camera_snapshot_example Console Script.

Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""


import sys
from meraki import meraki
import pprint


__author__ = "Sam Byers"
__email__ = "sabyers@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2019 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


# Generate a snapshot of what the camera sees at the specified time and return a link to that image.
# https://dashboard.meraki.com/api_docs#generate-a-snapshot-of-what-the-camera-sees-at-the-specified-time-and-return-a-link-to-that-image
def getcamerasnapshot(apikey, networkid, serialnumber, suppressprint=False):
    calltype = 'Camera'
    geturl = '{0}/networks/{1}/cameras/{2}/snapshot'.format(str(meraki.base_url),
                                                   str(networkid),
                                                   str(serialnumber))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = meraki.requests.get(geturl, headers=headers)
    #
    # Call return handler function to parse Dashboard response
    #
    result = meraki.__returnhandler(
        dashboard.status_code, dashboard.text, calltype, suppressprint)
    return result


def main(*args, **kwargs):

    pp = pprint.PrettyPrinter(width=50, compact=True)

    # Use your own API key for the Meraki dashboard API
    api_key = "your_api_key"

    my_orgs = meraki.myorgaccess(api_key)

    for org in my_orgs:
        if 'DevNet Sandbox' in org['name']:
            my_networks = meraki.getnetworklist(api_key, org['id'])
            break

    for network in my_networks:
        if 'DevNet Always On Read Only' in network['name']:
            my_net_devices = meraki.getnetworkdevices(api_key, network['id'])
            networkid = network['id']
            break

    for device in my_net_devices:
        if 'MV' in device['model']:
            camera_snapshot = getcamerasnapshot(api_key, networkid, device['serial'])
            break

    pp.pprint(camera_snapshot)


if __name__ == "__main__":
    sys.exit(main())
