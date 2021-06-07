#exit (0)
#region capture Calm variables
token = "@@{cred_Vault.secret}@@"
api_server = "@@{address}@@"
#endregion

# region prepare api call
api_server_port = "8200"
api_server_endpoint = "/v1/sys/policy/@@{tenant_prefix}@@.rw"
url = "http://{}:{}{}".format(
    api_server,
    api_server_port,
    api_server_endpoint
)
method = "PUT"
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-Vault-Token':token
}

# Compose the json payload
#payload = {"policy":"path \"secret/demo-env/@@{tenant_prefix}@@\" {capabilities = [\"list\",\"create\",\"read\",\"update\",\"delete\"]} "}
payload = {"policy":"path \"kv/data/tenants/@@{tenant_prefix}@@/*\" {\ncapabilities = [\"create\", \"update\", \"read\"]\n}\npath \"kv/delete/tenants/@@{tenant_prefix}@@/*\" {\ncapabilities = [\"delete\", \"update\"]\n}\npath \"kv/undelete/tenants/@@{tenant_prefix}@@/*\" {\ncapabilities = [\"update\"]\n}\npath \"kv/destroy/tenants/@@{tenant_prefix}@@/*\" {\ncapabilities = [\"update\"]\n}\npath \"kv/metadata/users/@@{tenant_prefix}@@/*\" {\ncapabilities = [\"list\", \"read\", \"delete\"]\n}\npath \"kv/metadata/\" {\ncapabilities = [\"list\"]\n}\npath \"kv/metadata/tenants/\" {\ncapabilities = [\"list\"]\n}\npath \"kv/data/shared/*\" {\ncapabilities = [\"read\"]\n}"}

# endregion

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