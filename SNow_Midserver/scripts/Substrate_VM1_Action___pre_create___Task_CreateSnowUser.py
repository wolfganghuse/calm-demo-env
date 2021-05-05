headers = {
        'Content-Type':'application/json', "Accept" : "application/json"
}
Snow_Instance = "@@{Snow_Instance}@@".split('//')[-1].split('/')[0]
Data={"user_name":"nucalmuser","first_name":"nucalmusr","last_name":"nucalmusr","title":"Administrative Assistant","department":"Development","user_password":"Snow@1234","active":"true","email":"xxx@xxx.com","mobile_phone":"9999999987"}
url = "https://{}/api/now/table/sys_user?sysparm_input_display_value=true".format(Snow_Instance)
resp = urlreq(url, verb="POST",params=json.dumps(Data),headers=headers,auth='BASIC', user="admin", passwd="@@{AdminPassword}@@", verify=False )
print(resp)

Data={"user":"nucalmusr nucalmusr",'role':'mid_server','state':"active"}
url = "https://{}/api/now/table/sys_user_has_role".format(Snow_Instance)
resp = urlreq(url, verb="POST",params=json.dumps(Data),headers=headers,auth='BASIC', user="admin", passwd="@@{AdminPassword}@@", verify=False )
print(resp)
