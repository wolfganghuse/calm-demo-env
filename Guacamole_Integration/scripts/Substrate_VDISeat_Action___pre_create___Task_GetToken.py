if @@{calm_array_index}@@>0:
  exit(0)

# Set  headers
headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}

# Get Cluster ID
url     = "https://@@{Guacamole_IP}@@/api/tokens?username=@@{GuacamoleCredential.username}@@&password=@@{GuacamoleCredential.secret}@@"
resp = urlreq(url, verb='POST', headers=headers)
if resp.ok:
  #print "CLUSTER_ID={0}".format(json.loads(resp.content)[0]['id'])
  print "authToken={0}".format(json.loads(resp.content)['authToken'])
else:
  print "Get authToken failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)