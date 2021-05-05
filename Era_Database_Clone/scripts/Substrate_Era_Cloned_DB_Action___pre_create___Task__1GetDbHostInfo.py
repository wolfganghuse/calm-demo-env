    # Set creds and headers
era_user = '@@{era_creds.username}@@'
era_pass = '@@{era_creds.secret}@@'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

# Set Time Machine ID by doing a GET on the Database
url  = "https://@@{era_ip}@@/era/v0.9/databases/@@{source_db_name}@@?value-type=name&detailed=true&load-dbserver-cluster=true"
resp = urlreq(url, verb='GET', auth='BASIC', user=era_user, passwd=era_pass, headers=headers)

# If the response is ok, set to our TM_ID variable
if resp.ok:
  print "TM_ID={0}".format(json.loads(resp.content)['timeMachineId'])
  print "SOURCE_DBSERVER_ID={0}".format(json.loads(resp.content)['databaseNodes'][0]['dbserver']['id'])

# If it is not, make a new call to get list of possible databases
else:
  print "Error: Database named '@@{source_db_name}@@' was not found."
  print ""
  print "The valid database_name values on this Era server are:"
  print "======================================================"
  
  url  = "https://@@{era_ip}@@:8443/era/v0.8/databases"
  resp = urlreq(url, verb='GET', auth='BASIC', user=era_user, passwd=era_pass, headers=headers)
  
  for dbs in json.loads(resp.content):
    if not dbs['clone']:
      print dbs['name']
  
  print "======================================================"
  print "Please use one of the above databases, and try again."
  exit(1)