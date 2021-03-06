# region headers
# * author:     salaheddine.gassim@nutanix.com
# * version:    v1.0/03032020 - initial version
# task_name:    FortigateCreateIpv4
# description:  Create an ipv4 address
# input vars:   vm_name, vm_ip
# output vars:  revision_changed
# endregion

# region capture Calm variables
api_server = "@@{fortigate_endpoint}@@"
fortigate_login = "@@{fortigate.username}@@"
fortigate_password = "@@{fortigate.secret}@@"
api_server_port = 80
vm_name = "@@{platform.spec.name}@@"
vm_ip = "@@{address}@@"
fortigate_vdom = "root"
# endregion

def fortiget_get_cookie(api_server, api_server_port, fortigate_login, fortigate_password):
    
    # region prepare api call
    api_server_endpoint = "/logincheck"
    url = "http://{}:{}{}".format(
        api_server,
        api_server_port,
        api_server_endpoint
    )
    method = "POST"
    headers = {
        'Accept': 'application/json'
    }
    auth_payload = "username=" + fortigate_login + "&secretkey=" + fortigate_password
    # endregion

    # region make api call
    # make the API call and capture the results in the variable called "resp"
    print("Making a {} API call to {}".format(method, url))
    resp = urlreq(url, verb=method, params=auth_payload,
                headers=headers, verify=False)

    # deal with the result/response
    if resp.ok:
        print("Successfully authenticated")
        my_cookie = resp.cookies.get_dict()
        return resp.cookies.get('ccsrftoken'), my_cookie
        
    else:
        print("Request failed")
        print("Headers: {}".format(headers))
        print('Status code: {}'.format(resp.status_code))
        print('Response: {}'.format(json.dumps(json.loads(resp.content), indent=4)))
        exit(1)
    # endregion


def fortiget_create_ip(api_server, api_server_port, fortigate_csrf_token, fortigate_cookie, vm_name, vm_ip, vdom="root"):
    
    # region prepare api call
    api_server_endpoint = "/api/v2/cmdb/firewall/address?&vdom=" + vdom
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
    create_payload = {"name": vm_name, "subnet": vm_ip + " 255.255.255.255"}

    # region make api call
    # make the API call and capture the results in the variable called "resp"
    print("Making a {} API call to {}".format(method, url))
    resp = urlreq(url, verb=method, params=json.dumps(create_payload), cookies=fortigate_cookie, headers=headers, verify=False)

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
    

fortigate_csrf_token, fortigate_cookie = fortiget_get_cookie(api_server,
                                                             api_server_port, fortigate_login, fortigate_password)
fortiget_create_ip(api_server, api_server_port, fortigate_csrf_token,
                   fortigate_cookie, vm_name, vm_ip, fortigate_vdom)
