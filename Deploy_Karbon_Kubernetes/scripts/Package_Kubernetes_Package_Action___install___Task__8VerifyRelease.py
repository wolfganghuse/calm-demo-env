# Set the headers, payload, and cookies
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
cookies = {'NTNX_IGW_SESSION': '@@{COOKIES}@@'}
payload = {}

# Set the address and make version call
url = "http://localhost:2081/k8srelease/portal/list"
resp = urlreq(url, verb='GET', cookies=cookies,
              headers=headers, verify=False)

# If the call went through successfully, check the available versions
if resp.ok:
  
  # Find our matching version and exit success
  for version in json.loads(resp.content):
    if version['version'] == "@@{k8s_version}@@":
      print("Success: @@{k8s_version}@@ is a valid Kubernetes version.")
      exit(0)

  # If we got this far, the version does not match
  print("Error: @@{k8s_version}@@ is NOT a valid Kubernetes version.")
  print("Supported Kubernetes versions on this release of Karbon are:")
  for version in json.loads(resp.content):
    print(version['version'])
  exit(1)

# If the call failed
else:
  print "Cluster create failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)