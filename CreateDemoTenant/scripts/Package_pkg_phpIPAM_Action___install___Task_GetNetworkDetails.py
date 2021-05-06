
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Token': '@@{cred_phpIPAM.secret}@@'}

# Fetch all VLANs and look for first unassigned

url = "https://@@{existing_phpIPAM.address}@@/api/@@{cred_phpIPAM.username}@@/subnets/@@{subnet_id}@@"
resp = urlreq(url, verb='GET', headers=headers, verify=False)
if resp.ok:
    subnet = json.loads(resp.content)['data']
    print "subnet={0}".format(subnet['calculation'])

        # If the call failed
else:
        print("Call failed"), json.dumps(json.loads(resp.content), indent=4)
        exit(1)
