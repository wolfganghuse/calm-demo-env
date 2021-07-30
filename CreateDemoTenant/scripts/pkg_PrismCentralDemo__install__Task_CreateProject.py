subnet_uuid = "@@{subnet_uuid}@@"
project_name = "@@{tenant_prefix}@@"
#region headers
# escript-template v20190611 / stephane.bourdeaud@nutanix.com
# * author:     MITU Bogdan Nicolae (EEAS-EXT) <Bogdan-Nicolae.MITU@ext.eeas.europa.eu>
# * version:    2019/09/17
# task_name:    CalmNewProject
# description:  Create a new project in different sizes: small, medium, large, configured with an unique VlanID, with project owner having the "Project Admin role".
# output vars:  project_name, project_uuid
# endregion

#region capture Calm variables
username = "@@{cred_PCDemo.username}@@"
username_secret = "@@{cred_PCDemo.secret}@@"
rand_num = "@@{calm_unique}@@"
calm_user_upn = "@@{calm_username}@@"
nutanix_calm_user_uuid = "@@{nutanix_calm_user_uuid}@@"
ahv_network_uuid = "@@{subnet_uuid}@@"
project_vlan_id = "@@{phpIPAM.vlan_number}@@"
project_size = "medium"
#input from user
user_project_name = "@@{tenant_prefix}@@"

account_uuid = "@@{UID}@@"
pcAccountUuid = '@@{PC_ACCOUNT_UUID}@@'
#endregion

#region define variables
project_name = "{0}_VPC{1}".format(user_project_name,project_vlan_id)
max_vcpu = 4
max_memory = 16*1073741824
max_storage = 200*1073741824
medium_multiplier = 2
large_multiplier = 4
if project_size == "medium":
   max_vcpu = max_vcpu*medium_multiplier
   max_memory = max_memory*medium_multiplier
   max_storage = max_storage*medium_multiplier   
if project_size == "large":
   max_vcpu = max_vcpu*large_multiplier
   max_memory = max_memory*large_multiplier
   max_storage = max_storage*large_multiplier 
# endregion

#region prepare api call
api_server = "@@{address}@@"
api_server_port = "9440"
api_server_endpoint = "/api/nutanix/v3/projects_internal"
length = 100
url = "https://{}:{}{}".format(
    api_server,
    api_server_port,
    api_server_endpoint
)
method = "POST"
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Compose the json payload
payload = {
    "api_version": "3.0",
    "metadata": {
        "kind": "project"
    },
    "spec": {
        "project_detail": {
            "name":project_name,
         	"description": "Project for Tenant {}, created on: xx".format(account_uuid),
            "resources": {
                "account_reference_list": [{
                    "uuid": pcAccountUuid,
                    "kind": "account",
                    "name": "nutanix_pc"
                }],
                "subnet_reference_list":[{
                	"kind":"subnet",
                  	"uuid":ahv_network_uuid
             	}],
            "external_network_list": [],
                "resource_domain":{
                   "resources":[
                      {
                         "limit":max_vcpu,
                         "resource_type":"VCPUS"
                      },
                      {
                         "limit":max_storage,
                         "resource_type":"STORAGE"
                      },
                      {
                         "limit":max_memory,
                         "resource_type":"MEMORY"
                      }
                   ]
	            },
            }
        },
        "user_list": [],
        "user_group_list": [],
        "access_control_policy_list": []
    }
}
# endregion

#region make the api call
print("Making a {} API call to {}".format(method, url))
resp = urlreq(
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

#region process the results
if resp.ok:
   print json.dumps(json.loads(resp.content), indent=4)
   print "project_name={0}".format(json.loads(resp.content)['spec']['project_detail']['name'])
   print "PROJECT_UUID={0}".format(json.loads(resp.content)['metadata']['uuid'])
   exit(0)
else:
    #api call failed
    print("Request failed")
    print("Headers: {}".format(headers))
    print("Payload: {}".format(json.dumps(payload)))
    print('Status code: {}'.format(resp.status_code))
    print('Response: {}'.format(json.dumps(json.loads(resp.content), indent=4)))
    exit(1)
# endregion
