# script

# modify these if required
cred_user = "@@{cred_centos_password.username}@@"
type = "Linux"

jwt = "@@{calm_jwt}@@"
vm_ip = "@@{address}@@"
blueprint_id = "@@{calm_blueprint_uuid}@@"

base_url = 'https://127.0.0.1:9440/api/nutanix/v3/'

def put_call(api_url, payload):
  headers = { 'Content-Type' : 'application/json', 'Accept':'application/json', 'Authorization': 'Bearer {}'.format(jwt) }
  r = urlreq(api_url, verb='PUT', params=payload, headers=headers, verify=False)
  resp = json.loads(r.content)
  if "status" in resp:
    return resp
  else:
    print "Post request failed", r.content
    exit(1)
    

def post_call(api_url, payload):
  headers = { 'Content-Type' : 'application/json', 'Accept':'application/json', 'Authorization': 'Bearer {}'.format(jwt) }
  r = urlreq(api_url, verb='POST', params=payload, headers=headers, verify=False)
  resp = json.loads(r.content)
  if "status" in resp:
    return resp
  else:
    print "Post request failed", r.content
    exit(1)
    
    
def get_call(api_url):
  headers = { 'Authorization': 'Bearer {}'.format(jwt) }
  r = urlreq(api_url, verb='GET', headers=headers, verify=False)
  resp = json.loads(r.content)
  if "status" in resp:
    return resp
  else:
    print "Post request failed", r.content
    exit(1)


api_url = base_url + "blueprints/" + '@@{calm_blueprint_uuid}@@'
blueprint = get_call(api_url)

project_id = blueprint["metadata"]["project_reference"]["uuid"]
project_name = blueprint["metadata"]["project_reference"]["name"]

api_url = base_url + "endpoints/import_json"

endpoint_json = {
  "spec": {
    "name": "Endpoint_@@{name}@@",
    "description": "Endpoint for vm @@{name}@@",
    "resources": {
      "name": "Endpoint_@@{name}@@",
      "type": type,
      "attrs": {
        "values": [ "@@{address}@@" ],
        "value_type": "IP",
        "port": 22,
        "credential_definition_list": [
          {
            "name": "endpoint_cred",
            "description": cred_user,
            "type": "KEY",
            "username": cred_user,
            "secret": {
              "attrs": {
                "is_secret_modified": False
              }
            }
          }
        ],
        "login_credential_reference": {
          "kind": "app_credential",
          "name": "endpoint_cred"
        }
      }
    }
  },
  "metadata": {
    "spec_version": 1,
    "name": "Endpoint_@@{name}@@",
    "kind": "endpoint",
    "project_reference": {
      "kind": "project",
      "uuid": project_id,
      "name": project_name
    }
  },
  "api_version": "3.0"
}

endpoint_return = post_call(api_url, json.dumps(endpoint_json))

api_url = base_url + "endpoints/" + endpoint_return["metadata"]["uuid"]
endpoint = get_call(api_url)

del endpoint["status"]
endpoint["spec"]["resources"]["attrs"]["credential_definition_list"][0]["secret"]["value"] = """@@{cred_centos_password.secret}@@"""
endpoint["spec"]["resources"]["attrs"]["credential_definition_list"][0]["secret"]["attrs"]["is_secret_modified"] = True 

endpoint_update = put_call(api_url, json.dumps(endpoint))

print "endpoint_uuid="+endpoint_return["metadata"]["uuid"]

