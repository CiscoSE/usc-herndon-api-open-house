#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""usc_herndon_api_open_house_meraki_example Console Script.

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


@click.command()
def main(*args, **kwargs):

    pp = pprint.PrettyPrinter(width=41, compact=True)

    # Use your own API key for the Meraki dashboard API
    api_key = ""

    my_orgs = meraki.myorgaccess(api_key)

    for org in my_orgs:
        if 'DevNet Sandbox' in org['name']:
            my_networks = meraki.getnetworklist(api_key, org['id'])
            break

    for network in my_networks:
        if 'DevNet Always On Read Only' in network['name']:
            my_vlans = meraki.getvlans(api_key, network['id'])
            break

    pp.pprint(my_vlans)


if __name__ == "__main__":
    sys.exit(main())
