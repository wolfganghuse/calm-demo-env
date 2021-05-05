# Set creds, headers, and URL
era_user = '@@{cred_era_admin_password.username}@@'
era_pass = '@@{cred_era_admin_password.secret}@@'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
url     = "https://@@{era_ip}@@/era/v0.9/operations/@@{DeleteOperationId}@@"
print "Monitoring Delete DatabaseVM Operation..."
# Monitor the operation
for x in range(20):
  
  print "Sleeping for 60 seconds."
  sleep(60)
  resp = urlreq(url, verb='GET', auth='BASIC', user=era_user, passwd=era_pass, headers=headers)
  print "Percentage Complete: {0}".format(json.loads(resp.content)['percentageComplete'])
  
  # If complete, break out of loop
  if json.loads(resp.content)['percentageComplete'] == "100":
    break

# If the operation did not complete within 20 minutes, assume it's not successful and error out
if json.loads(resp.content)['percentageComplete'] != "100":
  print "Get Operation ID timed out", json.dumps(json.loads(resp.content), indent=4)
  exit(1)
