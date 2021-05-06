headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

# Set the address and make cluster/list call
url = "https://@@{address}@@:9440/api/nutanix/v3/tasks/@@{task_uuid}@@"
resp = urlreq(url, verb='GET', user="@@{cred_PCDemo.username}@@", passwd="@@{cred_PCDemo.secret}@@", auth='BASIC', headers=headers, verify=False)

# If the call went through successfully, check the progress
if resp.ok:
  if (json.loads(resp.content)['status'] == "SUCCEEDED"):
    print("subnet_uuid={}".format(json.loads(resp.content)['entity_reference_list'][0]['uuid']))
    exit(0)
# If the call failed
else:
  print "Subnet UUID call failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)
