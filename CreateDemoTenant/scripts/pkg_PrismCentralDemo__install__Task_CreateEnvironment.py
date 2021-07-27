#script
jwt = '@@{calm_jwt}@@'
envuuid = "@@{UID}@@"
nameuuid = "@@{UID}@@"
cloudAccountUuid = "@@{CLOUD_ACCOUNT_UUID}@@"
envPassword = "@@{ENV_PASSWORD}@@"
projectUuid = "@@{PROJECT_UUID}@@"
pcAccountUuid = "@@{PC_ACCOUNT_UUID}@@"
ahv_network_uuid = "@@{subnet_uuid}@@"

api_server = "@@{address}@@"
api_server_port = "9440"
api_server_endpoint = "/api/nutanix/v3/environments"
length = 100
url = "https://{}:{}{}".format(
    api_server,
    api_server_port,
    api_server_endpoint
)
method = "POST"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer {}'.format(jwt)}


subnet_references = []

subnet = {
  "uuid": ahv_network_uuid
}
subnet_references.append(subnet)

payload = {
  "spec": {
    "name": nameuuid,
        "resources": {
            "substrate_definition_list": [{
                "variable_list": [],
                "type": "AHV_VM",
                "os_type": "Linux",
                "action_list": [],
                "create_spec": {
                    "name": "vm-@" + "@{calm_array_index}@" + "@-@" + "@{calm_time}@" + "@",
                    "resources": {
                        "disk_list": [{
                            "data_source_reference": {
                                "kind": "image",
                                "name": "Template_CentOS-7",
                                "uuid": "3b6c46f5-0ac0-4bab-8603-90ff9095066c"
                            },
                            "device_properties": {
                                "device_type": "DISK",
                                "disk_address": {
                                    "device_index": 0,
                                    "adapter_type": "SCSI"
                                }
                            }
                        }],
                        "memory_size_mib": 1024,
                        "num_sockets": 1,
                        "num_vcpus_per_socket": 1,
                        "account_uuid": cloudAccountUuid,
                        "boot_config": {
                            "boot_device": {
                                "disk_address": {
                                    "device_index": 0,
                                    "adapter_type": "SCSI"
                                }
                            }
                        },
                        "serial_port_list": [{
                            "index": 0,
                            "is_connected": False
                        }],
                        "nic_list": [{
                          "nic_type": "NORMAL_NIC",
                          "network_function_nic_type": "INGRESS",
                          "subnet_reference": {
                            "kind": "subnet",
                            "uuid": "@@{subnet_uuid}@@"
                          }
                        }]
                    },
                    "categories": {}
                },
                "name": "Untitled",
                "readiness_probe": {
                    "disable_readiness_probe": True
                },
                "editables": {
                    "create_spec": {
                        "resources": {
                            "nic_list": {},
                            "serial_port_list": {}
                        }
                    }
                },
                "uuid": str(uuid.uuid4())
            },
            {
                "variable_list": [],
                "type": "AHV_VM",
                "os_type": "Windows",
                "action_list": [],
                "create_spec": {
                    "name": "vm-@" + "@{calm_array_index}@" + "@-@" + "@{calm_time}@" + "@",
                    "resources": {
                        "disk_list": [{
                            "data_source_reference": {
                                "kind": "image",
                                "name": "Template_CentOS-7",
                                "uuid": "3b6c46f5-0ac0-4bab-8603-90ff9095066c"
                            },
                            "device_properties": {
                                "device_type": "DISK",
                                "disk_address": {
                                    "device_index": 0,
                                    "adapter_type": "SCSI"
                                }
                            }
                        }],
                        "memory_size_mib": 4096,
                        "num_sockets": 2,
                        "num_vcpus_per_socket": 2,
                        "account_uuid": cloudAccountUuid,
                        "boot_config": {
                            "boot_device": {
                                "disk_address": {
                                    "device_index": 0,
                                    "adapter_type": "SCSI"
                                }
                            }
                        },
                        "serial_port_list": [{
                            "index": 0,
                            "is_connected": False
                        }],
                        "nic_list": [{
                          "nic_type": "NORMAL_NIC",
                          "network_function_nic_type": "INGRESS",
                          "subnet_reference": {
                            "kind": "subnet",
                            "uuid": "@@{subnet_uuid}@@"
                          }
                        }]
                    },
                    "categories": {}
                },
                "name": "Untitled",
                "readiness_probe": {
                    "disable_readiness_probe": True
                },
                "editables": {
                    "create_spec": {
                        "resources": {
                            "nic_list": {},
                            "serial_port_list": {}
                        }
                    }
                },
                "uuid": str(uuid.uuid4())
            }],
            "credential_definition_list": [
                {
                    "username": "centos",
                    "secret": {
                        "attrs": {
                            "is_secret_modified": True
                        },
                        "value": "nutanix/4u"
                    },
                    "type": "PASSWORD",
                    "name": "Cred_OS",
                    "uuid": str(uuid.uuid4())
                },
                {
                    "username": "admin",
                    "secret": {
                        "attrs": {
                            "is_secret_modified": True
                        },
                        "value": "YNCntnx2021!"
                    },
                    "type": "PASSWORD",
                    "name": "PE_Creds",
                    "uuid": str(uuid.uuid4())
                },
                {
                    "username": "admin",
                    "secret": {
                        "attrs": {
                            "is_secret_modified": True
                        },
                        "value": "YNCntnx2021!"
                    },
                    "type": "PASSWORD",
                    "name": "PC_Creds",
                    "uuid": str(uuid.uuid4())
                },
                {
                    "username": "centos",
                    "secret": {
                        "attrs": {
                            "is_secret_modified": True
                        },
                        "value": "-----BEGIN RSA PRIVATE KEY-----\nMIIEpQIBAAKCAQEAzYpGCzUB9aWmHfSZyCZ83NfE0SyMgjjIGtkFYku6f4e+/tLC\n0GhHWjMD+Yqj8AquAVWrAuIpGL1ws4j45qMpCjwjSCmEzfmWFsiXmXgCqJWL7ZdC\nvA0HN3HcMSyVjObYb5FR865FFcdF6QRNqEwyzh5HL9VkN2B5MJ6+pT1ewkbuIisZ\njY4qjyU3iDDVS8+MO5SbAPTFSaeSXJMeXQHPma+OAyFP0sa4NROeZBcFmDkN3pBU\nhE05Nhlm0SB0oVzh2ffYdXS3ebiSXyVwDlt55pzcgV0/hqioBBdb/rZws8chEhQP\nITCww2ONAcSkBp3n1dqXBJH9XM5a9LRpQkBbwwIDAQABAoIBACzmA573GVJ7uOna\nQK2EGspzJ785qAfaN3wF5DMwr7CkCojHqV61KMD/W+Lq8hzBeHk6KX0bwjZxS2ks\nhpJ7Gb/umxZsW2JTHwIjF1qi6JHC+SoRXLaPcgAekyb6wkBhPO5CJFDCxLyZJyBb\nnEsjOgXkf1BnoNin7lE8nBCkc0qkp7BkQq3nOMzLvzLTilcUFxvSdRlL99uBC7uR\nJSpWQKCbxPhu0X2qQngKu3eHAYU4xA0Et0HLrltqaZIrTVp3xjC1JRiUbx/uMDzZ\nxSz+PsEdEkBqBq0kQIo7PchNfTXdmWQDhMHOqkL8c6l4v6xo2Rl8EAkvls1f9K6l\nRsZ38mECgYEA5pb451v5PuF1GWsQo5imzQcvsqUjOiduihyMZWFwgL5s9zTOQh/e\nQ35x1MuB9IsBL5xJBDMSf4cLlzzBjS7HU3cLVTJ8440/nR3xwBK9VHOoFaQvn6GL\njRa5d3cCQctYMUq456OTgO6VTDlGd23lTTID2YlrT6v28yT6p5e7v18CgYEA5DCk\nXzfFTAbfwXBDpr60C4bo7rqlY81yDdF/zpfwY0MvCJqc+rw2D9E4E81TdNRiQwKt\nF/rFReVCOTdwlIO7GMkBuXMB/XmlX8cRLK3OJXXkVi4ksyanH/YY3hnHHHcVCe3k\nwtOZ94JI8shp+5Q0m3TlO7TPRWKckonzT7nZEh0CgYEAz76MmMRAFerBuRjAcOOC\nw40J6ATna+lCqaN2yY+z8Amf2kf025YihORSYcjHWC4z71T6Y5IvxD1CsArIxg2y\n/vttdmB6K/iBq2fi+YzojkF02aqGTWcZdw9WIM9TdTtiRWZwmCDDL5HDaFzho4+a\n2qWI2l/4Elt3rS9Ps9X8DDkCgYEAwSi7uy5GgJjBB8m0Oo3rcmZ8/rhYECd0iGXy\nvjq3bg8M3Uej4ks3qCP+SCTipF6z3u2BAG9yVjw+1pgrYEwyMETWhNjpslsqteyY\niS2G9wbYhmsA/fWWOuPjIP7JITtcP890eccM6gsLHRixPhiyf3VwJh5j5eQXjaPg\npng3W7ECgYEAhQvzXcKR9VVydTnnQK05kRlmIDmhI7HF9sZF3UTJ9XzjbIj2UsS6\n+3PgCofuDYmPVzlMBAf6FwsjdprIZO/GYPKn9KyjHyGkCD2lopWX2HmdoeiKDFzX\nY0okOAvJl0Y2ffGa5oIMgxKUskjYc8MBpeBtqx/OV9WnT4LZ1obreI0=\n-----END RSA PRIVATE KEY-----"
                    },
                    "type": "KEY",
                    "name": "CENTOS",
                    "uuid": str(uuid.uuid4())
                }

            ],
            "infra_inclusion_list": [
                {
                    "account_reference": {
                        "uuid": pcAccountUuid,
                        "kind": "account"
                    },
                    "type": "nutanix_pc",
                    "subnet_references": subnet_references,
                    "default_subnet_reference": {
                        "uuid": ahv_network_uuid
                    }
                }
            ]
        }
    },
  "api_version": "3.0",
  "metadata": {
    "kind": "environment",
    "uuid": envuuid,
    "project_reference": {
      "kind": "project",
      "uuid": projectUuid
    }
  }
}

#region make the api call
print("Making a {} API call to {}".format(method, url))
r = urlreq(
    url,
    verb=method,
    params=json.dumps(payload),
    headers=headers,
    verify=False
)
# endregion

if r.ok:
    resp = json.loads(r.content)
    print("ENV_UUID={}".format(resp['metadata']['uuid']))
else:
    print("Post request failed", r.content)
    exit(1)
    
    
if r.ok:
    print r.content
    exit(0)

else:
    print("Post request failed", json.loads(r.content))
    print("Payload", json.dumps(payload))
    exit(1)
