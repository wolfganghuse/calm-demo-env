# Set creds and headers
era_user = '@@{era_creds.username}@@'
era_pass = '@@{era_creds.secret}@@'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

# Set the URL and payload
url     = "https://@@{era_ip}@@:8443/era/v0.8/clones/@@{CLONE_ID}@@/refresh"
payload = {
  "cloneId": "@@{CLONE_ID}@@",
  "snapshotId": "@@{VALIDATED_SNAP_ID}@@",
  "latestSnapshot": False,
  "timeZone": "UTC",
  "cloneInfo": [
    {
      "name": "working_dir",
      "value": "@@{WORKING_DIR}@@"
    }
  ]
}

# Make the call and set the response operation ID to the variable
resp = urlreq(url, verb='POST', auth='BASIC', user=era_user, passwd=era_pass, params=json.dumps(payload), headers=headers)
if resp.ok:
  print "REFRESH_OPERATION_ID={0}".format(json.loads(resp.content)['operationId'])
else:
  print "Post Database refresh request failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)