# Based on previous task, only create the cluster if it does not already exist
if "@@{CREATE_CLUSTER}@@" == "true":

  ## Create the Karbon Kubernetes cluster
  # Set the headers, payload, and cookies
  headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
  cookies = {'NTNX_IGW_SESSION': '@@{COOKIES}@@'}
  payload = {
  "cni_config": {
    "flannel_config": {
      "ip_pool_configs": [{
        "cidr":"172.20.0.0/16"
      }]
    },
    "node_cidr_mask_size": 24,
    "pod_ipv4_cidr": "172.20.0.0/16",
    "service_ipv4_cidr": "172.19.0.0/16"
  },
  "etcd_config": {
    "node_pools": [
      {
        "ahv_config": {
          "cpu": 4,
          "disk_mib": 40960,
          "memory_mib": 8192,
          "network_uuid": "@@{SUBNET_UUID}@@",
          "prism_element_cluster_uuid": "@@{CLUSTER_UUID}@@"
        },
        "name": "etcd-node-pool",
        "node_os_version": "@@{image_name}@@",
        "num_instances": 1
      }
    ]
  },
  "masters_config": {
    "single_master_config": {
      "external_ipv4_address": ""
    },
    "node_pools": [
      {
        "ahv_config": {
          "cpu": 8,
          "disk_mib": 122880,
          "memory_mib": 8192,
          "network_uuid": "@@{SUBNET_UUID}@@",
          "prism_element_cluster_uuid": "@@{CLUSTER_UUID}@@"
        },
        "name": "master-node-pool",
        "node_os_version": "@@{image_name}@@",
        "num_instances": 1
      }
    ]
  },
  "metadata": {
    "api_version": "v1.0.0"
  },
  "name": "@@{cluster_name}@@",
  "storage_class_config": {
    "default_storage_class": True,
    "name": "default-storageclass",
    "reclaim_policy": "Delete",
    "volumes_config": {
      "file_system": "ext4",
      "flash_mode": False,
      "password": "@@{PE_Creds.secret}@@",
      "prism_element_cluster_uuid": "@@{CLUSTER_UUID}@@",
      "storage_container": "SelfServiceContainer",
      "username": "@@{PE_Creds.username}@@"
    }
  },
  "version": "@@{k8s_version}@@",
  "workers_config": {
    "node_pools": [
      {
        "ahv_config": {
          "cpu": 8,
          "disk_mib": 122880,
          "memory_mib": 8192,
          "network_uuid": "@@{SUBNET_UUID}@@",
          "prism_element_cluster_uuid": "@@{CLUSTER_UUID}@@"
        },
        "name": "worker-node-pool",
        "node_os_version": "@@{image_name}@@",
        "num_instances": 2
      }
    ]
  }
}
  # Set the address and make images call
  url = "https://localhost:9440/karbon/v1/k8s/clusters"
  resp = urlreq(url, verb='POST', cookies=cookies,
                params=json.dumps(payload), headers=headers, verify=False)

  # If the call went through successfully, find the image by name
  if resp.ok:
    print("Cluster create was successful")
    spec = json.loads(resp.content)
    print("K8S_CLUSTER_UUID={0}".format(spec['cluster_uuid']))
    print("K8S_TASK_UUID={0}".format(spec['task_uuid']))
    exit(0)

  # If the call failed
  else:
    print "Cluster create failed", json.dumps(json.loads(resp.content), indent=4)
    exit(1)

else:
  print "Skipping cluster create"