
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Token': '@@{cred_phpIPAM.secret}@@'}


# release IP
print "gw_id={}".format("@@{gw_id}@@")
url = "https://@@{phpIPAM.address}@@/api/@@{cred_phpIPAM.username}@@/addresses/@@{gw_id}@@"
resp = urlreq(url, verb='DELETE', headers=headers, verify=False)
if resp.ok:
    print resp.content
else:
    print("Call failed"), json.dumps(json.loads(resp.content), indent=4)
    exit(1)