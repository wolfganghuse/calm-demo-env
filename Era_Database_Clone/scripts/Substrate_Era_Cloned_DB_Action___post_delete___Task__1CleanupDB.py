# Set creds and headers
era_user = '@@{era_creds.username}@@'
era_pass = '@@{era_creds.secret}@@'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

# Cleanup the DB and get Operation ID
url     = "https://@@{era_ip}@@:8443/era/v0.8/clones/@@{CLONE_ID}@@?cleanup=true&delete-db=true"
resp = urlreq(url, verb='DELETE', auth='BASIC', user=era_user, passwd=era_pass, headers=headers)
if resp.ok:
  print "CLEANUP_OPERATION_ID={0}".format(json.loads(resp.content)['operationId'])
  #print "Success!"
else:
  print "Cleanup Clone Operation failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)