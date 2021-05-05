# Set creds and headers
era_user = '@@{era_creds.username}@@'
era_pass = '@@{era_creds.secret}@@'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

# Get Time Machine Capability
url  = "https://@@{era_ip}@@:8443/era/v0.8/tms/@@{TM_ID}@@/clones/input-file?category=database%3Bvm_info"
resp = urlreq(url, verb='GET', auth='BASIC', user=era_user, passwd=era_pass, headers=headers)

if resp.ok:
  
  # Cycle through the various properties
  for property in json.loads(resp.content)['properties']:
    
    # Set the various variables
    if property['name'] == "vm_name":
      print "VM_NAME={0}".format(property['default_value'])
    elif property['name'] == "working_dir":
      print "WORKING_DIR={0}".format(property['default_value'])
    elif property['name'] == "era_deploy_base":
      print "ERA_BASE={0}".format(property['default_value'])

# In the event something went wrong with the API call
else:
  print "Get Input File request failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)