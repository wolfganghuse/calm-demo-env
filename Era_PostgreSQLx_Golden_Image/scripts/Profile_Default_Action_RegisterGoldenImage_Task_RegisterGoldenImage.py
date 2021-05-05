 # Set creds and headers
era_user = '@@{cred_era_admin_password.username}@@'
era_pass = '@@{cred_era_admin_password.secret}@@'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
print "Monitoring Register DatabaseVM Operation..."

# Set the URL and payload
url     = "https://@@{era_ip}@@/era/v0.9/dbservers/register"
payload = {
  "actionArguments": [
    {
      "name": "listener_port",
      "value": "5432"
    },
    {
      "name": "postgres_software_home",
      "value": "/usr/pgsql-@@{postgre_version}@@"
    }
  ],
  "vmIp": "@@{address}@@",
  "nxClusterUuid": "@@{CLUSTER_ID}@@",
  "databaseType": "postgres_database",
  "forcedInstall": "true",
  "workingDirectory": "/tmp",
  "username": "@@{cred_era_password.username}@@",
  "password": "@@{cred_era_password.secret}@@"
}

# Make the call and set the response operation ID to the variable
resp = urlreq(url, verb='POST', auth='BASIC', user=era_user, passwd=era_pass, params=json.dumps(payload), headers=headers)
if resp.ok:
  print "REGISTER_OPERATION_ID={0}".format(json.loads(resp.content)['operationId'])
else:
  print "Database VM Register failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)