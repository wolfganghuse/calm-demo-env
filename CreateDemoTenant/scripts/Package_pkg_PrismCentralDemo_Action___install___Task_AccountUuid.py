
#region capture Calm variables
username = '@@{cred_PCDemo.username}@@'
username_secret = "@@{cred_PCDemo.secret}@@"
api_server = "@@{address}@@"
entity_name = "NTNX_LOCAL_AZ"

#endregion

#region define variables
environment_uuids = []
#endregion

# region prepare api call
api_server_port = "9440"
api_server_endpoint = "/api/nutanix/v3/accounts/list"
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
payload = {"length": length}
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
    for entity in json_resp["entities"]:
        if entity["status"]["name"] == entity_name:
            print ("nutanix_calm_account_uuid={}").format(entity["metadata"]["uuid"])
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