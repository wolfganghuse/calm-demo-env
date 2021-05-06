# region capture Calm variables
tenant_gw_ip = @@{phpIPAM.subnet}@@['Min host IP']
tenant_dhcp_ip = @@{phpIPAM.subnet}@@['Max host IP']
tenant_subnet = @@{phpIPAM.subnet}@@['Network']
tenant_bitmask = @@{phpIPAM.subnet}@@['Subnet bitmask']

api_server = "@@{address}@@"
api_server_port = 80
interface_name = "Tenant {}".format("@@{tenant_prefix}@@")
interface_ip = "{0}/{1}".format(tenant_gw_ip,tenant_bitmask)
interface_port = "port2"
interface_vlan = "@@{phpIPAM.vlan_number}@@"
fortigate_vdom = "root"
fortigate_csrf_token = @@{fortigate_csrf_token}@@
fortigate_cookie = @@{fortigate_cookie}@@
# endregion



def fortigate_create_Interface(api_server, api_server_port, fortigate_csrf_token, fortigate_cookie, name, ip, port ,vlanId, vdom="root"):
    
  # region prepare api call
  api_server_endpoint = "/api/v2/cmdb/system/interface"
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
    "name": name,
    "vdom": {
      "q_origin_key": vdom
    },
    "ip": ip,
    "allowaccess": "https ping ssh",
    "interface": {
      "q_origin_key": port
    },
    "vlanid": vlanId,
    "device-identification": "enable",
    "lldp-transmission": "enable",
    "role": "lan",
    "fortilink-split-interface": "disable"
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
      print("interface_name={}".format(interface_name))
  else:
      print("Request failed")
      print("Headers: {}".format(headers))
      print('Status code: {}'.format(resp.status_code))
      print('Response: {}'.format(json.dumps(json.loads(resp.content), indent=4)))
      exit(1)
    # endregion




fortigate_create_Interface(api_server, api_server_port, fortigate_csrf_token, fortigate_cookie, interface_name, interface_ip, interface_port, interface_vlan,  fortigate_vdom)