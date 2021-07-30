#script
username = "@@{cred_PCDemo.username}@@"
username_secret = "@@{cred_PCDemo.secret}@@"
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
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}


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
                                "name": "CentOS7",
                                "uuid": "7241ee32-dae1-43c0-8c3c-3e697325dcd9"
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
                                "name": "Windows2016",
                                "uuid": "c046f2c4-49c5-4cb7-a7f5-ce1dcc628d15"
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
                        "value": "nutanix/4u"
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
                        "value": "nutanix/4u"
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
                        "value": "xxx"
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
    auth='BASIC',
    user=username,
    passwd=username_secret,
    params=json.dumps(payload),
    headers=headers,
    verify=False
)
# endregion

if r.ok:
    resp = json.loads(r.content)
    print("ENV_UUID={}".format(resp['metadata']['uuid']))
else:
    # print the content of the response (which should have the error message)
    print("Request failed", json.dumps(
        json.loads(r.content),
        indent=4
    ))
    print("Headers: {}".format(headers))
    print("Payload: {}".format(payload))
    exit(1)
# endregion