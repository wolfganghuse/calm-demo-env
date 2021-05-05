# Set the headers, payload, and cookies
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
cookies = {'NTNX_IGW_SESSION': '@@{COOKIES}@@'}
payload = {
  "cluster_uuids":[
    "@@{K8S_CLUSTER_UUID}@@"
  ]
}

# Loop for 20 minutes, do a GET every 30 seconds
for x in range(40):
  
  # Set the address and make cluster/list call
  url = "https://localhost:7050/karbon/acs/k8s/cluster/list"
  resp = urlreq(url, verb='POST', cookies=cookies,
                params=json.dumps(payload), headers=headers, verify=False)

  # If the call went through successfully, check the progress
  if resp.ok:

    for cluster in json.loads(resp.content):
      if cluster["task_uuid"] == "@@{K8S_TASK_UUID}@@":
        if cluster["task_progress_percent"] == 100:
          print("Kubernetes cluster deployed successfully.")
          exit(0)
        else:
          print("Kubernetes cluster progress: " + str(cluster["task_progress_percent"]))
    
    print("Sleeping for 30 seconds")
    sleep(30)

  # If the call failed
  else:
    print "Cluster list call failed", json.dumps(json.loads(resp.content), indent=4)
    exit(1)
    
# If we got to this point, the cluster didn't create in 20 minutes, so error out
else:
  print "Cluster was not created in 20 minutes, errroring out.", json.dumps(json.loads(resp.content), indent=4)
  exit(1)