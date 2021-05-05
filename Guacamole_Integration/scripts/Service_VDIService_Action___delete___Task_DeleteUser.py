# Set  headers
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

url     = "https://@@{Guacamole_IP}@@/api/session/data/mysql/users/@@{VDIUser}@@?token=@@{calm_array_authToken}@@"
resp = urlreq(url, verb='DELETE', headers=headers)
if resp.ok:
  #print "CLUSTER_ID={0}".format(json.loads(resp.content)[0]['id'])
  print resp.content
else:
  print "Delete Group failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)
 