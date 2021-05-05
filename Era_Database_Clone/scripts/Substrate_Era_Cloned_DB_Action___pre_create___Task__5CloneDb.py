# Set creds and headers
era_user = '@@{era_creds.username}@@'
era_pass = '@@{era_creds.secret}@@'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

# Set the Clone DB Name
if "@@{cloned_db_name}@@" == "":
  cloneName = '@@{source_db_name}@@_Clone_@@{calm_time("%Y%m%d%H%M")}@@'
else:
  cloneName = "@@{cloned_db_name}@@"

# Set the URL and payload
url     = "https://@@{era_ip}@@:8443/era/v0.8/tms/@@{TM_ID}@@/clones"
payload = {
  "snapshotId": "@@{VALIDATED_SNAP_ID}@@",
  "cloneDescription": "Clone of '@@{source_db_name}@@' managed through Calm application @@{calm_application_name}@@",
  "timeZone": "UTC",
  "cloneName": cloneName,
  "cloneInfo": [
    {
      "name": "db_password",
      "value": "@@{cloned_db_password}@@"
    },
    {
      "name": "vm_name",
      "value": "@@{VM_NAME}@@"
    },
    {
      "name": "client_public_key",
      "value": "@@{db_server_creds.public_key}@@"
    },
    {
      "name": "working_dir",
      "value": "@@{WORKING_DIR}@@"
    },
    {
      "name": "era_deploy_base",
      "value": "@@{ERA_BASE}@@"
    },
    {
      "name": "create_dbserver",
      "value": True
    },
    {
      "name": "compute_profile_id",
      "value": "@@{COMPUTE_PROFILE_ID}@@"
    },
    {
      "name": "network_profile_id",
      "value": "@@{NETWORK_PROFILE_ID}@@"
    },
    {
      "name": "db_parameter_profile_id",
      "value": "@@{DB_PROFILE_ID}@@"
    }
  ],
  "timeMachineId": "@@{TM_ID}@@",
  "latestSnapshot": False
}

# Make the call and set the response operation ID to the variable
resp = urlreq(url, verb='POST', auth='BASIC', user=era_user, passwd=era_pass, params=json.dumps(payload), headers=headers)
if resp.ok:
  print "CLONE_OPERATION_ID={0}".format(json.loads(resp.content)['operationId'])
else:
  print "Post Database clone request failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)