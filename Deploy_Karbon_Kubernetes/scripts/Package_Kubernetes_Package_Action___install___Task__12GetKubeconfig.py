# Set the headers, payload, and cookies
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
cookies = {'NTNX_IGW_SESSION': '@@{COOKIES}@@'}

# Set the address and make kubeconfig call
url = "https://localhost:7050/acs/k8s/cluster/@@{K8S_CLUSTER_UUID}@@/kubeconfig"
resp = urlreq(url, verb='GET', cookies=cookies, headers=headers, verify=False)

# If the call went through successfully, print out the kubeconfig
if resp.ok:
  print "KUBECONFIG={0}".format(json.loads(resp.content)['yml_config'])
  exit(0)

# If the call failed
else:
  print "Get kubeconfig failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)