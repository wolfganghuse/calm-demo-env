#script
jwt = '@@{calm_jwt}@@'
ROLE_ADMIN = '@@{ROLE_ADMIN}@@'
ROLE_OPERATOR = '@@{ROLE_OPERATOR}@@'
DOMAIN = '@@{DOMAIN}@@'
ROOT_OU = '@@{ROOT_OU}@@'

# convert domain name to Microsoft AD path
# -----------------------------------------------------------
def get_role_uuid(role_name):
  api_url = 'https://localhost:9440/api/nutanix/v3/roles/list'
  headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer {}'.format(jwt)}
  payload = {
      'filter': 'name=={}'.format(role_name),
      'kind': 'role',
      'offset': 0
  }
  r = urlreq(api_url, verb='POST', params=json.dumps(payload), headers=headers, verify=False)
  result = json.loads(r.content)
  if result['entities']:
      return result['entities'][0]['metadata']['uuid']
  else:
      return None


admin_role_uuid = get_role_uuid(ROLE_ADMIN)
operator_role_uuid = get_role_uuid(ROLE_OPERATOR)

uid = uuid.uuid4()
print("UID={}".format(uid))
print('ROLE_ADMIN_UUID={}'.format(admin_role_uuid))
print('ROLE_OPERATOR_UUID={}'.format(operator_role_uuid))
