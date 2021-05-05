## Get Karbon Image UUID
# Set the jwt, headers and payload

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
payload = {'length': 100}
cookies = {'NTNX_IGW_SESSION': '@@{COOKIES}@@'}

# Set the address and make images call
url = "https://localhost:9440/api/nutanix/v3/images/list"
resp = urlreq(url, verb='POST', cookies=cookies,
              params=json.dumps(payload), headers=headers, verify=False)

# If the call went through successfully, set the cookie and then find the image by name
if resp.ok:
  for entity in json.loads(resp.content)['entities']:
    if entity['status']['name'] == 'karbon-@@{image_name}@@':
      print "IMAGE_UUID={0}".format(entity['metadata']['uuid'])
      exit(0)

# If the call failed
else:
  print "Images call failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)

# If we made it this far, there was an error
print "ERROR: '@@{image_name}@@' image was not found."
exit(0)