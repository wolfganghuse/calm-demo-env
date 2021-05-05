#script
#eScript

headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Token': '@@{phpIPAM_token}@@'}
#payload = "{\"description\": \"lab201 Pod CIDR\"}"
url = "https://@@{phpIPAM_address}@@/api/Calm/sections/Customers"
resp = urlreq(url, verb='GET', headers=headers, verify=False)
if resp.ok:
    section_id = json.loads(resp.content)['data']['id']

# If the call failed
else:
    print("Call failed"), json.dumps(json.loads(resp.content), indent=4)
    exit(1)

# Fetch Subnet-IDs for LoadBalancer and POD/Service CIDR

url = "https://@@{phpIPAM_address}@@/api/Calm/sections/{0}/subnets".format(section_id)
resp = urlreq(url, verb='GET', headers=headers, verify=False)
if resp.ok:
    for subnet in json.loads(resp.content)['data']:
        if subnet['description'] == "@@{subnet}@@":
            id = subnet['id']
            print "phpipam_subnet_id={0}".format(id)
            

# If the call failed
else:
        print("Call failed"), json.dumps(json.loads(resp.content), indent=4)
        exit(1)
