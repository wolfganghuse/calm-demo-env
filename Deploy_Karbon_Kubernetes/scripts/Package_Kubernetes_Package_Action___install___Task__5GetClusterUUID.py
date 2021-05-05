## Get Karbon Image UUID
# Set the headers, payload, and cookies
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
payload = {}
cookies = {'NTNX_IGW_SESSION': '@@{COOKIES}@@'}

# Set the address and make subnets call
url = "https://localhost:9440/api/nutanix/v3/subnets/@@{SUBNET_UUID}@@"
resp = urlreq(url, verb='GET', cookies=cookies,
              params=json.dumps(payload), headers=headers, verify=False)

# If the call went through successfully, set the cluster_ref UUID
if resp.ok:
  spec = json.loads(resp.content)['spec']
  print "CLUSTER_UUID={0}".format(spec['cluster_reference']['uuid'])
  exit(0)

# If the call failed
else:
  print "Projects call failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)

# If we made it this far, there was an error
print "ERROR: something went wrong."
exit(0)