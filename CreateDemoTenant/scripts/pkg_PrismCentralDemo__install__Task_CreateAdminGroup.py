#script
Distinguished_Name = '@@{TenantAD.Distinguished_Name}@@'
username = "@@{cred_PCDemo.username}@@"
username_secret = "@@{cred_PCDemo.secret}@@"
api_server = "@@{address}@@"
api_server_port = "9440"
api_server_endpoint = "/api/nutanix/v3/user_groups"

length = 100
url = "https://{}:{}{}".format(
    api_server,
    api_server_port,
    api_server_endpoint
)

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
method = "POST"
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
if r.ok:
    resp = json.loads(r.content)
    print("GROUP_ADMIN_UUID={}".format(resp['metadata']['uuid']))

else:
    # print the content of the response (which should have the error message)
    print("Request failed", json.dumps(
        json.loads(r.content),
        indent=4
    ))
    print("Headers: {}".format(headers))
    print("Payload: {}".format(payload))
    exit(1)
# endregion