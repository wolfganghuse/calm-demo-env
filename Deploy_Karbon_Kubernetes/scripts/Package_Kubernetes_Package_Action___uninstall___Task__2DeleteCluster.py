## Delete the Karbon Kubernetes cluster
# Set the headers, payload, and cookies
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
cookies = {'NTNX_IGW_SESSION': '@@{COOKIES}@@'}

# Set the address and make images call
url = "https://localhost:9440/karbon/v1/k8s/clusters/@@{K8S_CLUSTER_UUID}@@"
resp = urlreq(url, verb='DELETE', cookies=cookies,
              headers=headers, verify=False)

# If the call went through successfully, find the image by name
if resp.ok:
  print("Cluster delete was successful")
  spec = json.loads(resp.content)
  exit(0)

# If the call failed
else:
  print "Cluster delete failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)