
# Set  headers
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
payload = '[{"op":"add","path":"/connectionGroupPermissions/@@{calm_array_ParentGroup}@@","value":"READ"},{"op":"add","path":"/connectionGroupPermissions/@@{calm_array_GroupIdentifier}@@","value":"READ"},{"op":"add","path":"/connectionPermissions/@@{ConnectionIdentifier}@@","value":"READ"}]'

url     = "https://@@{Guacamole_IP}@@//api/session/data/mysql/users/@@{VDIUser}@@/permissions?token=@@{calm_array_authToken}@@"
resp = urlreq(url, verb='PATCH', headers=headers,params=payload,send_form_encoded_data='FALSE')
if resp.ok:
  print resp.content
  #print "GroupIdentifier={0}".format(json.loads(resp.content)['identifier'])
else:
  print "Add Connection failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)