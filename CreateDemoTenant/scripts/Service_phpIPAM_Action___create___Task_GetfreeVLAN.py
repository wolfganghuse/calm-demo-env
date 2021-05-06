
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Token': '@@{cred_phpIPAM.secret}@@'}

# Fetch all VLANs and look for first unassigned

url = "https://@@{existing_phpIPAM.address}@@/api/@@{cred_phpIPAM.username}@@/vlan"
resp = urlreq(url, verb='GET', headers=headers, verify=False)
vlan_found = False
if resp.ok:
    for vlan in json.loads(resp.content)['data']:
        if vlan['custom_tenant'] == "0":
            id = vlan['vlanId']
            number = vlan['number']
            print "vlan_id={0}".format(id)
            print "vlan_number={0}".format(number)
            vlan_found = True
            break
    if not vlan_found:
        print ("No free VLAN found")
        exit (1)

# If the call failed
else:
        print("Call failed"), json.dumps(json.loads(resp.content), indent=4)
        exit(1)
