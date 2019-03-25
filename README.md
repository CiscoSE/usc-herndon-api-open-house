# usc_herndon_api_open_house_meraki_example

*Code for a Meraki API activity at a USC API Open House Event in Herndon, VA*

---

## Motivation

This script is an example for participants in the Meraki API activity at the API Tech Open House in Herndon, VA.

## Show Me!

``` Python
python usc_herndon_api_open_house_meraki_example.py
Organization Operation Successful - See returned data for results

Network Operation Successful - See returned data for results

VLANs Operation Successful - See returned data for results

[{'applianceIp': '192.168.128.1',
  'dhcpBootFilename': None,
  'dhcpBootNextServer': None,
  'dhcpBootOptionsEnabled': False,
  'dhcpHandling': 'Run a DHCP server',
  'dhcpLeaseTime': '1 day',
  'dhcpOptions': [],
  'dnsNameservers': 'upstream_dns',
  'fixedIpAssignments': {},
  'id': 1,
  'name': 'Default',
  'networkId': 'L_646829496481099586',
  'reservedIpRanges': [],
  'subnet': '192.168.128.0/24'}]
```

## Features

Include a succinct summary of the features/capabilities of your project.

- Print list of VLANs in a meraki network using the meraki Python module

## Technologies & Frameworks Used

This is Cisco Sample Code! In this small example script we're using the meraki Python module.

**Cisco Products & Services:**

- Meraki Dashboard API

**Third-Party Products & Services:**

- requests

**Tools & Frameworks:**

- [Meraki Python Module](https://github.com/meraki/dashboard-api-python)

## Usage

python usc_herndon_api_open_house_meraki_example.py

## Installation

- pip install -r requirements.txt
- git clone https://github.com/CiscoSE/usc_herndon_api_open_house_meraki_example

## Authors & Maintainers

Smart people responsible for the creation and maintenance of this project:

- Sam Byers <sabyers@cisco.com>
- Kory Wood <kowood@cisco.com>

## Credits

Meraki for making an easy to use Python module.

## License

This project is licensed to you under the terms of the [Cisco Sample
Code License](./LICENSE).
