#region headers
# escript-template v20190611 / stephane.bourdeaud@nutanix.com
# * author:     stephane.bourdeaud@nutanix.com
# * version:    2019/09/17
# task_name:    CalmGetEnvUuid
# description:  Get existing project environments from Calm.
# output vars:  environment_uuid
# endregion

#region capture Calm variables
username = '@@{cred_PCDemo.username}@@'
username_secret = "@@{cred_PCDemo.secret}@@"
api_server = "@@{address}@@"
#endregion

#region define variables
environment_uuids = []
#endregion

# region prepare api call
api_server_port = "9440"
api_server_endpoint = "/api/nutanix/v3/users/list"
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

# Compose the json payload
payload = {
  "kind": "user",
  "offset": 0,
  "length": length
}
# endregion

#region make the api call
print("Making a {} API call to {}".format(method, url))
resp = urlreq(
    url,
    verb=method,
    auth='BASIC',
    user=username,
    passwd=username_secret,
    params=json.dumps(payload),
    headers=headers,
    verify=False
)
#endregion

#region process the results
if resp.ok:
    json_resp = json.loads(resp.content)
    for user in json_resp['entities']:
        if user['status']['name'] == "@@{calm_username}@@":
            user['metadata']['uuid']
            #environment_uuids.append(environment['metadata']['uuid'])
            print("nutanix_calm_user_uuid={}").format(user['metadata']['uuid'])
            exit(0)
else:
    # print the content of the response (which should have the error message)
    print("Request failed", json.dumps(
        json.loads(resp.content),
        indent=4
    ))
    print("Headers: {}".format(headers))
    print("Payload: {}".format(payload))
    exit(1)
# endregion