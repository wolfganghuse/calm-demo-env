#script
jwt = '@@{calm_jwt}@@'

# Get PC IP and PE uuid
api_url = 'https://localhost:9440/api/nutanix/v3/user_groups/@@{GROUP_ADMIN_UUID}@@'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer {}'.format(jwt)}

r = urlreq(api_url, verb='DELETE', headers=headers, verify=False)
if r.ok:
    resp = json.loads(r.content)

else:
    print("Post request failed", r.content)
    exit(1)
