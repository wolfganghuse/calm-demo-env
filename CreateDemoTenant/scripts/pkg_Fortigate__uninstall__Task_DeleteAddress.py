# region capture Calm variables

api_server = "@@{Fortigate.address}@@"
api_server_port = 80
interface_name = "Tenant {}".format("@@{tenant_prefix}@@")
fortigate_vdom = "root"
fortigate_csrf_token = @@{fortigate_csrf_token}@@
fortigate_cookie = @@{fortigate_cookie}@@
# endregion



def fortigate_delete_Address(api_server, api_server_port, fortigate_csrf_token, fortigate_cookie, name, vdom="root"):
    
  # region prepare api call
  api_server_endpoint = "/api/v2/cmdb/firewall/address/{}".format(name)
  url = "http://{}:{}{}".format(
      api_server,
      api_server_port,
      api_server_endpoint
  )
  method = "DELETE"
  fortigate_csrf_token = fortigate_csrf_token.replace('"','')
  headers = {
      'Accept': '*/*',
      'X-CSRFTOKEN': fortigate_csrf_token
  }
  # endregion
  

  # region make api call
  # make the API call and capture the results in the variable called "resp"
  print("Making a {} API call to {}".format(method, url))
  resp = urlreq(url, verb=method, cookies=fortigate_cookie, headers=headers, verify=False)

  # deal with the result/response
  if resp.ok:
      print("Request was successful. Status code: {}".format(resp.status_code))
      result = json.loads(resp.content)
      print("revision_changed : {}".format(result['revision_changed']))
  else:
      print("Request failed")
      print("Headers: {}".format(headers))
      print('Status code: {}'.format(resp.status_code))
      print('Response: {}'.format(json.dumps(json.loads(resp.content), indent=4)))
      exit(1)
    # endregion




fortigate_delete_Address(api_server, api_server_port, fortigate_csrf_token, fortigate_cookie, interface_name,  fortigate_vdom)