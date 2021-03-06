task_uuid = "@@{task_uuid}@@"
username = "@@{cred_PCDemo.username}@@"
username_secret = "@@{cred_PCDemo.secret}@@"
api_server = "@@{address}@@"
api_server_port = "9440"
api_server_endpoint = "/api/nutanix/v3/tasks/{}".format(task_uuid)

length = 100
url = "https://{}:{}{}".format(
    api_server,
    api_server_port,
    api_server_endpoint
)

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
method = "GET"

#region make the api call
print("Making a {} API call to {}".format(method, url))
r = urlreq(
    url,
    verb=method,
    auth='BASIC',
    user=username,
    passwd=username_secret,
    headers=headers,
    verify=False
)
# endregion


# If the call went through successfully, check the progress
if r.ok:
  if (json.loads(r.content)['status'] == "SUCCEEDED"):
    print("project_uuid={}".format(json.loads(r.content)['entity_reference_list'][0]['uuid']))
    exit(0)
# If the call failed
# If the call failed
else:
    # print the content of the response (which should have the error message)
    print("Request failed", json.dumps(
        json.loads(r.content),
        indent=4
    ))
    print("Headers: {}".format(headers))
    exit(1)
# endregion