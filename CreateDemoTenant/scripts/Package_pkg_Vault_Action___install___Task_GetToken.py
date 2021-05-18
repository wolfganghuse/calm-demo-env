exit (0)
#region capture Calm variables
token = "@@{cred_Vault.secret}@@"
api_server = "@@{address}@@"
#endregion

# region prepare api call
api_server_port = "8200"
api_server_endpoint = "/auth/token/create"
url = "http://{}:{}{}".format(
    api_server,
    api_server_port,
    api_server_endpoint
)
method = "POST"
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-Vault-Token':token
}

# Compose the json payload
payload = {
  "policies": ["@@{tenant_prefix}@@.rw"],
  "renewable": true
}# endregion

#region make the api call
print("Making a {} API call to {}".format(method, url))
resp = urlreq(
    url,
    verb=method,
    params=json.dumps(payload),
    headers=headers,
    verify=False
)
#endregion

#region process the results
if resp.ok:
    print ("vault_token={0}".format(json.loads(resp.content)['auth']['client_token']['name']))
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