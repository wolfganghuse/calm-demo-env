## Get Karbon Image UUID
# Set the headers, payload, and cookies
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
payload = {"length": 100}
cookies = {'NTNX_IGW_SESSION': '@@{COOKIES}@@'}

# Make the image/portal/list call
url = "http://localhost:2081/image/portal/list"
resp = urlreq(url, verb='GET', cookies=cookies,
              headers=headers, verify=False)

# Get the image uuid
if resp.ok:
  for image in json.loads(resp.content):
    if image['version'] == '@@{image_name}@@':
      image_uuid = image['uuid']
else:
  print "image/portal/list call failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)
  
# Loop for 10 minutes, do a GET every 30 seconds
for x in range(20):
  
  # Make an image/list call, regardless of downloaded/downloading state
  url = "https://localhost:9440/karbon/acs/image/list"
  resp = urlreq(url, verb='GET', cookies=cookies,
                headers=headers, verify=False)

  # If the call was successful, loop through the images (there may be more than one)
  if resp.ok:
    for image in json.loads(resp.content):
      print(json.dumps(image, indent=4))
      # If this is our image, print status
      if image['version'] == '@@{image_name}@@':
        print "\nImage:  'karbon-" + image['version'] + "'"
        print "Status: '" + image['status'] + "'"
        
        # If the image is available, download it
        if image['status'] == 'Available':
          
          print "\nKarbon image not found. Downloading now."
          payload = {"uuid": image_uuid}
          url = "http://localhost:2081/image/download"
          resp = urlreq(url, verb='POST', cookies=cookies,
                        params=json.dumps(payload), headers=headers, verify=False)
          
          # If the call went through successfully, set the new url, then loop
          if resp.ok:
            print "Image download started."
          else:
            print "Image download call failed. Erroring out."
            exit(1)
        
        # If the image is downloaded, exit successfully
        elif image['status'] == 'Downloaded':
          print "IMAGE_UUID={0}".format(image['uuid'])
          print "OS_FLAVOR={0}".format(image['os_flavor'])
          print "Image successfully downloaded.  Exiting."
          exit(0)
      
  else:
    print "Image list call failed.  Erroring out."
    exit(1)
        
  print "Sleeping for 30 seconds"
  sleep(30)

# If we made it this far, assume the download failed
print "The Karbon image was not downloaded in 10 minutes. Erroring out."
exit(1)