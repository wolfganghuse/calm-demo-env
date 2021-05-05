## Open the Karbon UI to set the cookies
# Set the headers, payload, and creds
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
pc_user = '@@{PC_Creds.username}@@'
pc_pass = '@@{PC_Creds.secret}@@'
payload = {
  "action_on_failure":"CONTINUE",
  "execution_order":"SEQUENTIAL",
  "api_request_list":[
    {
      "operation":"GET",
      "path_and_params":"/api/nutanix/v3/users/me"
    },
    {
      "operation":"GET",
      "path_and_params":"/api/nutanix/v3/users/info"
    }
  ],
  "api_version":"3.0"
}

url = "https://localhost:9440/karbon/prism/api/nutanix/v3/batch"
resp = urlreq(url, verb='POST', params=json.dumps(payload), headers=headers,
              auth='BASIC', user=pc_user, passwd=pc_pass, verify=False)

# If the call went through successfully
if resp.ok:
  
  # Set the cookie
  print "COOKIES={0}".format(resp.cookies['NTNX_IGW_SESSION'])

# If the Karbon UI batch call failed
else:
  print "The Karbon UI batch call failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)