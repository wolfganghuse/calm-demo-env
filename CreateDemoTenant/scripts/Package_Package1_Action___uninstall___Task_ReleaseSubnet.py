
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Token': '@@{cred_phpIPAM.secret}@@'}

        
url = "https://@@{phpIPAM.address}@@/api/@@{cred_phpIPAM.username}@@/subnets/@@{subnet_id}@@"
resp = urlreq(url, verb='DELETE', headers=headers, verify=False)
if resp.ok:
    print resp.content

# If the call failed
else:
        print("Call failed"), json.dumps(json.loads(resp.content), indent=4)
        exit(1)
