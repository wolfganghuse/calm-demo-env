# Set creds and headers
era_user = '@@{era_creds.username}@@'
era_pass = '@@{era_creds.secret}@@'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

# Get Time Machine Capability
url  = "https://@@{era_ip}@@:8443/era/v0.9/dbservers/@@{SOURCE_DBSERVER_ID}@@?value-type=id&load-dbserver-cluster=false&load-databases=true&load-clones=false&load-metrics=false&detailed=true&curator=false&time-zone=UTC"
resp = urlreq(url, verb='GET', auth='BASIC', user=era_user, passwd=era_pass, headers=headers)

if resp.ok:
  
  # Cycle through the various properties
  for property in json.loads(resp.content)['properties']:
    
    # Set the various variables
    if property['name'] == "compute_profile_id":
      print "COMPUTE_PROFILE_ID={0}".format(property['value'])
    elif property['name'] == "network_profile_id":
      print "NETWORK_PROFILE_ID={0}".format(property['value'])
    elif property['name'] == "db_parameter_profile_id":
      print "DB_PROFILE_ID={0}".format(property['value'])

  for property in json.loads(resp.content)['databases'][0]['properties']:
    # Set the various variables
    if property['name'] == "db_parameter_profile_id":
      print "DB_PROFILE_ID={0}".format(property['value'])

# In the event something went wrong with the API call
else:
  print "Get Input File request failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)