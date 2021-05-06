#script
#eScript
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Token': '@@{cred_phpIPAM.secret}@@'}

# Fetch Section ID

url = "https://@@{existing_phpIPAM.address}@@/api/@@{cred_phpIPAM.username}@@/sections/@@{phpIPAM_section}@@"
resp = urlreq(url, verb='GET', headers=headers, verify=False)
if resp.ok:
    section_id = json.loads(resp.content)['data']['id']

# If the call failed
else:
    print("Call failed"), json.dumps(json.loads(resp.content), indent=4)
    exit(1)

# Fetch Subnet-ID
url = "https://@@{existing_phpIPAM.address}@@/api/@@{cred_phpIPAM.username}@@/sections/{0}/subnets".format(section_id)
resp = urlreq(url, verb='GET', headers=headers, verify=False)
if resp.ok:
    for subnet in json.loads(resp.content)['data']:
        if subnet['description'] == "@@{phpIPAM_network_space}@@":
            subnet_id = subnet['id']
# If the call failed
else:
    print("Call failed"), json.dumps(json.loads(resp.content), indent=4)
    exit(1)

# Get first free Subnet and assign to Tenant and VLAN

payload = {"custom_tenant":"@@{tenant_prefix}@@","vlanId":"@@{vlan_id}@@","description":"Auto-Assigned by Calm to @@{tenant_prefix}@@"}
url = "https://@@{existing_phpIPAM.address}@@/api/@@{cred_phpIPAM.username}@@/subnets/{0}/first_subnet/24/".format(subnet_id)
resp = urlreq(url, verb='POST', params=json.dumps(payload), headers=headers, verify=False)

if resp.ok:
    print "subnet_id={0}".format(json.loads(resp.content)['id'])
    
# If the call failed
else:
    print("Call failed"), json.dumps(json.loads(resp.content), indent=4)
    exit(1)

