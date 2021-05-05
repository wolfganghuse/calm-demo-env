# Set creds and headers
era_user = "@@{cred_era_admin_password.username}@@"
era_pass = "@@{cred_era_admin_password.secret}@@"
headers = {"Content-Type": "application/json", "Accept": "application/json"}

# Get Cluster ID
url = "https://@@{era_ip}@@/era/v0.9/clusters"
resp = urlreq(
    url, verb="GET", auth="BASIC", user=era_user, passwd=era_pass, headers=headers
)
if resp.ok:
    print("CLUSTER_ID={0}".format(json.loads(resp.content)[0]["id"]))
else:
    print(
        "Get Cluster ID request failed", json.dumps(json.loads(resp.content), indent=4)
    )
    exit(1)