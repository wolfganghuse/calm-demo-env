username = "@@{cred_PCDemo.username}@@"
username_secret = "@@{cred_PCDemo.secret}@@"

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
user_project_name = "@@{tenant_prefix}@@"
project_vlan_id = @@{phpIPAM.vlan_number}@@

tenant_dhcp_range = "{0} {1}".format(tenant_dhcp_min,tenant_dhcp_max)
subnet_name = "{0}_VPC{1}".format(user_project_name,project_vlan_id)

api_server = "@@{address}@@"
api_server_port = "9440"
api_server_endpoint = "/api/nutanix/v3/subnets"

length = 100
url = "https://{}:{}{}".format(
    api_server,
    api_server_port,
    api_server_endpoint
)

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
method = "POST"

# Assign found Subnet to Tenant
payload = {
   "spec":{
      "name":subnet_name,
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
                  "8.8.8.8"
               ]
            }
         },
         "vlan_id":project_vlan_id,
         "virtual_switch_uuid":"e777f435-ccd4-405f-bcff-108ff6dcff49"
      },
      "cluster_reference":{
         "kind":"cluster",
         "name":"YNC-POC",
         "uuid":"0005c56b-b51d-f36f-4e1b-ac1f6b35f44a"
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
#region make the api call
print("Making a {} API call to {}".format(method, url))
r = urlreq(
    url,
    verb=method,
    auth='BASIC',
    user=username,
    passwd=username_secret,
    headers=headers,
    verify=False
)
# endregion

#region process the results
if r.ok:
   print json.dumps(json.loads(r.content), indent=4)
   print "subnet_name={0}".format(json.loads(r.content)['spec']['name'])
   print "subnet_uuid={0}".format(json.loads(r.content)['metadata']['uuid'])
   exit(0)
# If the call failed
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