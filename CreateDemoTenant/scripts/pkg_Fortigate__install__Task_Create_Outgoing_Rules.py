# region capture Calm variables

api_server = "@@{address}@@"
api_server_port = 80
interface_name = "@@{interface_name}@@"
fortigate_vdom = "root"
fortigate_csrf_token = @@{fortigate_csrf_token}@@
fortigate_cookie = @@{fortigate_cookie}@@
# endregion


def fortigate_create_Address(api_server, api_server_port, fortigate_csrf_token, fortigate_cookie, name, vdom="root"):
    
  # region prepare api call
  api_server_endpoint = "/api/v2/cmdb/firewall/policy"
  url = "http://{}:{}{}".format(
      api_server,
      api_server_port,
      api_server_endpoint
  )
  method = "POST"
  fortigate_csrf_token = fortigate_csrf_token.replace('"','')
  headers = {
      'Accept': '*/*',
      'X-CSRFTOKEN': fortigate_csrf_token
  }
  # endregion
    
  create_payload = {
    "name": name+" Outgoing",
    "dstintf":[
          {
            "name": "port1"
          }
    ],
    "srcintf":[
          {
            "name": name
          }
    ],
    "dstaddr": [
      {
        "name": "all"
      }
    ],
    "srcaddr": [
      {
        "name": name+ " address"
      }
    ],
    "action": "accept",
    "schedule": {
      "q_origin_key": "always"
    },
    "nat": "enable",
    "service": [
      {
        "name": "ALL"
      }
    ]
    
  }

  print (create_payload)

  # region make api call
  # make the API call and capture the results in the variable called "resp"
  print("Making a {} API call to {}".format(method, url))
  resp = urlreq(url, verb=method, params=json.dumps(create_payload), cookies=fortigate_cookie, headers=headers, verify=False)

  # deal with the result/response
  if resp.ok:
      print("Request was successful. Status code: {}".format(resp.status_code))
      result = json.loads(resp.content)
      print("Response : {}".format(result))
      print("fortigate_out_id={}".format(result['mkey']))
  else:
      print("Request failed")
      print("Headers: {}".format(headers))
      print('Status code: {}'.format(resp.status_code))
      print('Response: {}'.format(json.dumps(json.loads(resp.content), indent=4)))
      exit(1)
    # endregion

fortigate_create_Address(api_server, api_server_port, fortigate_csrf_token, fortigate_cookie, interface_name, fortigate_vdom)