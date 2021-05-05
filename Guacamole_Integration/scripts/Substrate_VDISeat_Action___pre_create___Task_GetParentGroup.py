if @@{calm_array_index}@@>0:
  exit(0)

# Set  headers
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

# Get Cluster ID
url     = "https://@@{Guacamole_IP}@@/api/session/data/mysql/connectionGroups?token=@@{authToken}@@"
resp = urlreq(url, verb='GET', headers=headers)
if resp.ok:
  #print "CLUSTER_ID={0}".format(json.loads(resp.content)[0]['id'])
  #print "authToken={0}".format(json.loads(resp.content)['authToken'])
  ParentGroup=-1
  for Group in json.loads(resp.content):
    if json.loads(resp.content)[Group]['name']=='@@{GuacamoleGroup}@@':
      ParentGroup=Group
      print "ParentGroup={0}".format(ParentGroup)
  if ParentGroup==-1:
    print "@@{GuacamoleGroup}@@ not found"
    exit(1)
else:
  print "Get Groups failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)