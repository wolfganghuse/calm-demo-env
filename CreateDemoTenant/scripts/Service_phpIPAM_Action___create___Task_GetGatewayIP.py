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
        if subnet['description'] == "@@{phpIPAM_gw_space}@@":
            subnet_id = subnet['id']
# If the call failed
else:
    print("Call failed"), json.dumps(json.loads(resp.content), indent=4)
    exit(1)

# Fetch free IP from Subnet

payload = {"description":"@@{tenant_prefix}@@","custom_tenant":"@@{tenant_prefix}@@"}
url = "https://@@{existing_phpIPAM.address}@@/api/@@{cred_phpIPAM.username}@@/addresses/first_free/{0}/".format(subnet_id)
resp = urlreq(url, verb='POST', params=json.dumps(payload), headers=headers, verify=False)
if resp.ok:
  gw_ip = json.loads(resp.content)
  free_gw_id = gw_ip['id']
  free_gw_ip = gw_ip['data']
  print "gw_id={0}".format(free_gw_id)
  print "gw_ip={0}".format(free_gw_ip)
# If the call failed
else:
  print("Call failed"), json.dumps(json.loads(resp.content), indent=4)
  exit(1)

