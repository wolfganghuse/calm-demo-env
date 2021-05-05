# Set creds and headers
#prism_user = '@@{PrismElement.username}@@'
#prism_pass = '@@{PrismElement.secret}@@'

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
payload ='{ "kind": "image" }'
#url     = "https://@@{PrismElement_IP}@@:@@{PrismElement_Port}@@/PrismGateway/services/rest/v2.0/storage_containers/"
url = "https://172.23.0.15:9440/api/nutanix/v3/images/list"

#resp = urlreq(url, verb='GET', auth='BASIC', user=prism_user, passwd=prism_pass, headers=headers)
resp = urlreq(url, verb='POST', auth='BASIC', user='sa_prism_local', passwd='Nutanix/4u', headers=headers, params=payload)
if resp.ok:
  for image in json.loads(resp.content)['entities']:
    print image['status']['name']+","
 