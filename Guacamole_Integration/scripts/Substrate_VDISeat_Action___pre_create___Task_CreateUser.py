
# Set  headers
VDIUser = "@@{SessionName}@@@@{calm_array_index}@@"
VDIPass = _construct_random_password(lower=5,puncs="")
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
payload = '{"username":"'+VDIUser+'","password":"'+VDIPass+'","attributes":{"disabled":"","expired":"","access-window-start":"","access-window-end":"","valid-from":"","valid-until":"","timezone":null}}'
print payload
# Get Cluster ID
url     = "https://@@{Guacamole_IP}@@/api/session/data/mysql/users?token=@@{calm_array_authToken}@@"
resp = urlreq(url, verb='POST', headers=headers,params=payload,send_form_encoded_data='FALSE')
if resp.ok:
  print "VDIUser="+VDIUser
  print "VDIPass="+VDIPass
  #print "GroupIdentifier={0}".format(json.loads(resp.content)['identifier'])
else:
  print "Create USser failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)