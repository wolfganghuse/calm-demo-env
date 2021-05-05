# script
jwt = "@@{calm_jwt}@@"
vm_ip = "@@{address}@@"
blueprint_id = "@@{calm_blueprint_uuid}@@"

base_url = 'https://127.0.0.1:9440/api/nutanix/v3/'
  
def delete_call(api_url):
  headers = { 'Authorization': 'Bearer {}'.format(jwt) }
  r = urlreq(api_url, verb='DELETE', headers=headers, verify=False)
  resp = json.loads(r.content)
  return resp

api_url = base_url + "endpoints/@@{endpoint_uuid}@@"
delete_call(api_url)