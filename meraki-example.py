from meraki import meraki
import pprint

pp = pprint.PrettyPrinter(width=41, compact=True)

# This API key is for the Meraki sandbox that is open to the public
api_key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"

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
