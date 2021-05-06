
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Token': '@@{cred_phpIPAM.secret}@@'}


# Get VLAN-Details
url = "https://@@{existing_phpIPAM.address}@@/api/@@{cred_phpIPAM.username}@@/vlan/@@{vlan_id}@@"
resp = urlreq(url, verb='GET', headers=headers, verify=False)
if resp.ok:
    vlan = json.loads(resp.content)["data"]
else:
    print("Call failed"), json.dumps(json.loads(resp.content), indent=4)
    exit(1)
    
# Assign found VLAN to Tenant
payload = {"custom_tenant":"@@{tenant_prefix}@@","name":vlan['name']}

url = "https://@@{existing_phpIPAM.address}@@/api/@@{cred_phpIPAM.username}@@/vlan/@@{vlan_id}@@"

resp = urlreq(url, verb='PATCH', params=json.dumps(payload), headers=headers, verify=False)
if resp.ok:
    print resp.content

# If the call failed
else:
        print("Call failed"), json.dumps(json.loads(resp.content), indent=4)
        exit(1)
