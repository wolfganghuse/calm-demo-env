if @@{calm_array_index}@@>0:
  exit(0)

# Set  headers
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
payload = '{"parentIdentifier":"@@{ParentGroup}@@","name":"@@{SessionName}@@","type":"ORGANIZATIONAL","attributes":{"max-connections":"","max-connections-per-user":"","enable-session-affinity":""}}'
# Get Cluster ID
url     = "https://@@{Guacamole_IP}@@/api/session/data/mysql/connectionGroups?token=@@{authToken}@@"
resp = urlreq(url, verb='POST', headers=headers,params=payload,send_form_encoded_data='FALSE')
if resp.ok:
  print "GroupIdentifier={0}".format(json.loads(resp.content)['identifier'])
else:
  print "Create Groups failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)