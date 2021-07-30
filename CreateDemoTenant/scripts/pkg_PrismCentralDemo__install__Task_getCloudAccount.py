account_name = 'NTNX_LOCAL_AZ'
username = "@@{cred_PCDemo.username}@@"
username_secret = "@@{cred_PCDemo.secret}@@"
api_server = "@@{address}@@"
api_server_port = "9440"
api_server_endpoint = "/api/nutanix/v3/accounts/list"

length = 100
url = "https://{}:{}{}".format(
    api_server,
    api_server_port,
    api_server_endpoint
)

payload = {
    'filter': 'state!=DELETED;state!=DRAFT;name=={}'.format(account_name)
}
method = "POST"
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

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

if r.ok:
    resp = json.loads(r.content)
    for account in resp['entities']:
      if account['metadata']['name'] == account_name:
          print("CLOUD_ACCOUNT_UUID={}".format(account['status']['resources']['data']['cluster_account_reference_list'][0]['uuid']))
          print("PC_ACCOUNT_UUID={}".format(account['metadata']['uuid']))
# If the call failed
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