#script
jwt = '@@{calm_jwt}@@'
Distinguished_Name = '@@{TenantAD.Distinguished_Name}@@'

# Get PC IP and PE uuid
api_url = 'https://localhost:9440/api/nutanix/v3/user_groups'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer {}'.format(jwt)}

payload = {
    "spec": {
        "resources": {
            "directory_service_user_group": {
                "distinguished_name": "cn={}-ADMIN,{}".format("@@{tenant_prefix}@@",Distinguished_Name)
            }
        }
    },
    "metadata": {
        "kind": "user_group"
    }
}

r = urlreq(api_url, verb='POST', params=json.dumps(payload), headers=headers, verify=False)
if r.ok:
    resp = json.loads(r.content)
    print("GROUP_ADMIN_UUID={}".format(resp['metadata']['uuid']))

else:
    print("Post request failed", r.content)
    exit(1)
