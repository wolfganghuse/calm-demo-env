subnet_uuid = "@@{subnet_uuid}@@"
project_name = "@@{tenant_prefix}@@"

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}


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
        
url = "https://@@{existing_PrismCentralDemo.address}@@:9440/api/nutanix/v3/projects"
resp = urlreq(url, verb='POST', params=json.dumps(payload), auth='BASIC', user="@@{cred_PCDemo.username}@@", passwd="@@{cred_PCDemo.secret}@@", headers=headers, verify=False)
if resp.ok:
    print resp.content
    print "task_uuid={0}".format(json.loads(resp.content)['status']['execution_context']['task_uuid'])

# If the call failed
else:
        print("Call failed"), json.dumps(json.loads(resp.content), indent=4)
        exit(1)
