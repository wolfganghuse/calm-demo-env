## Create the Karbon Kubernetes cluster
# Set the headers, payload, and cookies
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
cookies = {'NTNX_IGW_SESSION': '@@{COOKIES}@@'}
payload = {}

# Set the address and make images call
url = "http://localhost:2081/k8s/cluster/list"
resp = urlreq(url, verb='POST', cookies=cookies,
              params=json.dumps(payload), headers=headers, verify=False)

# If the call went through successfully, check the names of the clusters
if resp.ok:

  create_cluster = True
  
  for cluster in json.loads(resp.content):
    print(cluster)
    if cluster['cluster_metadata']['name'] == '@@{cluster_name}@@':
      print("CREATE_CLUSTER=false")
      print("K8S_CLUSTER_UUID={0}".format(spec['cluster_uuid']))
      create_cluster = False
  
  if create_cluster:
    print "CREATE_CLUSTER=true"

  exit(0)

# If the call failed
else:
  print "Cluster create failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)