import requests
# Set creds and headers
era_user = "@@{cred_era_admin_password.username}@@"
era_pass = "@@{cred_era_admin_password.secret}@@"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

eracleanupdbvmurl = "https://@@{era_ip}@@/era/v0.9/dbservers/@@{SOURCE_DBSERVER_ID}@@"
# Set headers
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
# Define payload
payload = json.dumps({
    "softRemove": False,
    "remove": True,
    "delete": False,
    "deleteVgs": True,
    "deleteVmSnapshots": True
})
#
resp = requests.delete(
    eracleanupdbvmurl,
    headers=headers,
    auth=(era_user, era_pass),
    data= payload,
    verify=False
)


if resp.ok:
    print("DeleteOperationId={0}".format(json.loads(resp.content)[0]["operationId"]))
else:
    print(
        "Delete DatabaseVM failed", json.dumps(json.loads(resp.content), indent=4)
    )
    exit(1)
