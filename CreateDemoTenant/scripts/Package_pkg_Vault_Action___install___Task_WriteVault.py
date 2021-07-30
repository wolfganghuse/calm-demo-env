headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-Vault-Token': '@@{cred_Vault.secret}@@'}
values = @@{phpIPAM.subnet}@@
values["vlan_number"]="@@{phpIPAM.vlan_number}@@"
values["gateway"]="@@{phpIPAM.gw_ip}@@"
values["network_uuid"]="@@{PrismCentralDemo.subnet_uuid}@@"
values["subnet_name"]="@@{PrismCentralDemo.subnet_name}@@"

print values
payload = {"data":values}
print payload

url = "http://@@{address}@@:8200/v1/kv/data/tenants/@@{tenant_prefix}@@/subnet"
resp = urlreq(url, verb='POST',params=json.dumps(payload), headers=headers, verify=False)
if resp.ok:
    print resp.content

# If the call failed
else:
    print("Call failed"), json.dumps(json.loads(resp.content), indent=4)
    exit(1)
