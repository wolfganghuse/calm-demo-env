headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

# Loop for 2 minutes, do a GET every 10 seconds
for x in range(12):
  
  # Set the address and make cluster/list call
  url = "https://@@{address}@@:9440/api/nutanix/v3/tasks/@@{task_uuid}@@"
  resp = urlreq(url, verb='GET', user="@@{cred_PCDemo.username}@@", passwd="@@{cred_PCDemo.secret}@@", auth='BASIC', headers=headers, verify=False)

  # If the call went through successfully, check the progress
  if resp.ok:
    if (json.loads(resp.content)['status'] == "FAILED"):
      print "Job failed", json.dumps(json.loads(resp.content), indent=4)
      exit(1)
    if (json.loads(resp.content)['status'] == "SUCCEEDED"):
      print("subnet_uuid={}".format(json.loads(resp.content)['entity_reference_list'][0]['uuid']))
      exit(0)
    else:
      print("Subnet Create progress: {}".format(json.loads(resp.content)["percentage_complete"]))
    print("Sleeping for 10 seconds")
    sleep(10)

  # If the call failed
  else:
    print "Subnet Create call failed", json.dumps(json.loads(resp.content), indent=4)
    exit(1)
    
# If we got to this point, the cluster didn't create in 20 minutes, so error out
else:
  print "Subnet was not created in 2 minutes, errroring out.", json.dumps(json.loads(resp.content), indent=4)
  exit(1)
