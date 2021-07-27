subnet_uuid = "@@{subnet_uuid}@@"
project_name = "@@{tenant_prefix}@@"
username = "@@{cred_PCDemo.username}@@"
username_secret = "@@{cred_PCDemo.secret}@@"
api_server = "@@{address}@@"
api_server_port = "9440"
api_server_endpoint = "/api/nutanix/v3/projects"

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
      "name":project_name,
      "resources":{
         "subnet_reference_list":[
            {
               "kind":"subnet",
               "uuid":subnet_uuid
            }
         ],
         "user_reference_list":[
            
         ],
         "external_user_group_reference_list":[
            {
               "kind":"user_group",
               "uuid":"eb89479c-d1d0-45c9-9854-a72d8d51a1be",
               "name":"cn=lab_users,cn=users,dc=ntnx,dc=test"
            }
         ]
      }
   },
   "api_version":"3.1.0",
   "metadata":{
      "use_categories_mapping":False,
      "kind":"project",
      "categories_mapping":{
         
      },
      "should_force_translate":True,
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

if r.ok:
    print r.content
    print "task_uuid={0}".format(json.loads(r.content)['status']['execution_context']['task_uuid'])

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