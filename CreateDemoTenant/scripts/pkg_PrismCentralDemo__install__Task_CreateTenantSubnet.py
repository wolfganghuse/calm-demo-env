#Calculate needed Addresses
dhcp_min = 100
dhcp_max = 200
tenant_gw_ip = @@{phpIPAM.subnet}@@['Min host IP']
tenant_dhcp_ip = @@{phpIPAM.subnet}@@['Max host IP']
tenant_subnet = @@{phpIPAM.subnet}@@['Network']
tenant_bitmask = @@{phpIPAM.subnet}@@['Subnet bitmask']
tenant_subnet_split = tenant_subnet.split(".")
tenant_dhcp_min = "{0}.{1}.{2}.{3}".format(tenant_subnet_split[0],tenant_subnet_split[1],tenant_subnet_split[2],int(tenant_subnet_split[3])+dhcp_min)
tenant_dhcp_max = "{0}.{1}.{2}.{3}".format(tenant_subnet_split[0],tenant_subnet_split[1],tenant_subnet_split[2],int(tenant_subnet_split[3])+dhcp_max)

tenant_dhcp_range = "{0} {1}".format(tenant_dhcp_min,tenant_dhcp_max)


headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}


# Assign found Subnet to Tenant
payload = {
   "spec":{
      "name":"Subnet @@{tenant_prefix}@@",
      "resources":{
         "vswitch_name":"br0",
         "subnet_type":"VLAN",
         "ip_config":{
            "default_gateway_ip":tenant_gw_ip,
            "dhcp_server_address":{
               "ip":tenant_dhcp_ip
            },
            "pool_list":[
               {
                  "range":tenant_dhcp_range
               }
            ],
            "prefix_length":int(tenant_bitmask),
            "subnet_ip":tenant_subnet,
            "dhcp_options":{
               "domain_name_server_list":[
                  tenant_gw_ip
               ]
            }
         },
         "vlan_id":@@{phpIPAM.vlan_number}@@,
         "virtual_switch_uuid":"eb87a234-6ed5-482c-9f80-5c531317437b"
      },
      "cluster_reference":{
         "kind":"cluster",
         "name":"NTNX-DEMO01",
         "uuid":"0005c16a-854c-d5b0-30dd-ac1f6bcd62c7"
      }
   },
   "metadata":{
      "kind":"subnet",
      "categories_mapping":{
         
      },
      "categories":{
         
      }
   }
}
        
url = "https://@@{existing_PrismCentralDemo.address}@@:9440/api/nutanix/v3/subnets"
resp = urlreq(url, verb='POST', params=json.dumps(payload), auth='BASIC', user="@@{cred_PCDemo.username}@@", passwd="@@{cred_PCDemo.secret}@@", headers=headers, verify=False)
if resp.ok:
    print resp.content
    print "task_uuid={0}".format(json.loads(resp.content)['status']['execution_context']['task_uuid'])

# If the call failed
else:
        print("Call failed"), json.dumps(json.loads(resp.content), indent=4)
        exit(1)
