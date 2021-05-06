
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Token': '@@{cred_phpIPAM.secret}@@'}


# Assign found Subnet to Tenant
payload = {"id":"@@{subnet_id}@@","custom_tenant":"@@{tenant_prefix}@@","vlanId":"@@{vlan_id}@@"}
        
url = "https://@@{existing_phpIPAM.address}@@/api/@@{cred_phpIPAM.username}@@/subnets"
resp = urlreq(url, verb='PATCH', params=json.dumps(payload), headers=headers, verify=False)
if resp.ok:
    print resp.content

# If the call failed
else:
        print("Call failed"), json.dumps(json.loads(resp.content), indent=4)
        exit(1)
