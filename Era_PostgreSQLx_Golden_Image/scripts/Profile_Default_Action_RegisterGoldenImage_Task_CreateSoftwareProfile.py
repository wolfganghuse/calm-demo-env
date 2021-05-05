# Set creds and headers
era_user = '@@{cred_era_admin_password.username}@@'
era_pass = '@@{cred_era_admin_password.secret}@@'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
print "Monitoring Create Software Profile Operation..."

# Set the URL and payload
url     = "https://@@{era_ip}@@/era/v0.9/profiles"
payload = {
  "engineType": "postgres_database",
  "type": "Software",
  "topology": "single",
  "dbVersion": "ALL",
  "systemProfile": "false",
  "properties": [
    {
      "name": "SOURCE_DBSERVER_ID",
      "value": "@@{SOURCE_DBSERVER_ID}@@",
      "secure": "false",
      "description": "ID of the database server that should be used as a reference to create the software profile"
    },
    {
      "name": "BASE_PROFILE_VERSION_NAME",
      "value": "Postgres @@{postgre_version}@@ by Calm Blueprint",
      "secure": "false",
      "description": "Name of the base profile version."
    },
    {
      "name": "BASE_PROFILE_VERSION_DESCRIPTION",
      "value": "Deployed by Calm @@{calm_application_name}@@",
      "secure": "false",
      "description": "Description of the base profile version."
    },
    {
      "name": "OS_NOTES",
      "value": "",
      "secure": "false",
      "description": "Notes or description for the Operating System."
    },
    {
      "name": "DB_SOFTWARE_NOTES",
      "value": "",
      "secure": "false",
      "description": "Description of the Postgres database software."
    }
  ],
  "availableClusterIds": [
    "@@{CLUSTER_ID}@@"
  ],
  "name": "@@{calm_application_name}@@"
}

# Make the call and set the response operation ID to the variable
resp = urlreq(url, verb='POST', auth='BASIC', user=era_user, passwd=era_pass, params=json.dumps(payload), headers=headers)
if resp.ok:
  print "CREATEPROFILE_OPERATION_ID={0}".format(json.loads(resp.content)['operationId'])
else:
  print "Create Profile failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)