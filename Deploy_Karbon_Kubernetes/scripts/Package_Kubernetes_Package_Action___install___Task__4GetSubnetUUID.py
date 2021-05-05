## Get Karbon Image UUID
# Set the headers, payload, and cookies
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
payload = {}
cookies = {'NTNX_IGW_SESSION': '@@{COOKIES}@@'}

# Set the address and make projects call
url = "https://localhost:9440/api/nutanix/v3/projects/list"
resp = urlreq(url, verb='POST', cookies=cookies,
              params=json.dumps(payload), headers=headers, verify=False)

# If the call went through successfully, find the project by name
if resp.ok:
  for entity in json.loads(resp.content)['entities']:
    if entity['status']['name'] == '@@{calm_project_name}@@':
      for subnet in entity['status']['resources']['subnet_reference_list']:
        if subnet['name'] == '@@{network_name}@@':
          print "SUBNET_UUID={0}".format(subnet['uuid'])
          exit(0)
      else:
        print "Network '@@{network_name}@@' is not available in project '@@{calm_project_name}@@'.  Please check the network name and try again."
        exit(1)

# If the call failed
else:
  print "Projects call failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)

# If we made it this far, there was an error
print "ERROR: '@@{calm_project_name}@@' project was not found."
exit(0)