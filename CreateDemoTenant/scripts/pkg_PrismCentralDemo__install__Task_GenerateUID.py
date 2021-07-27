#script
username = "@@{cred_PCDemo.username}@@"
username_secret = "@@{cred_PCDemo.secret}@@"
pc_address = "@@{address}@@"

ROLE_ADMIN = '@@{ROLE_ADMIN}@@'
ROLE_OPERATOR = '@@{ROLE_OPERATOR}@@'
DOMAIN = '@@{DOMAIN}@@'
ROOT_OU = '@@{ROOT_OU}@@'

# convert domain name to Microsoft AD path
# -----------------------------------------------------------
def get_role_uuid(role_name):
    api_server = "@@{address}@@"
    api_server_port = "9440"
    api_server_endpoint = "/api/nutanix/v3/roles/list"
    length = 100
    url = "https://{}:{}{}".format(
        api_server,
        api_server_port,
        api_server_endpoint
    )
    method = "POST"
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
  
    payload = {
        'filter': 'name=={}'.format(role_name),
        'kind': 'role',
        'offset': 0
    }
    
    #region make the api call
    print("Making a {} API call to {}".format(method, url))
    r = urlreq(
        url,
        verb=method,
        auth='BASIC',
        user=username,
        passwd=username_secret,
        params=json.dumps(payload),
        headers=headers,
        verify=False
    )
    # endregion
    
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
