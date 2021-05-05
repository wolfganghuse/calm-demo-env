#script

print ("Downloading AS3 Extensions...")
as3 = urlreq("@@{AS3}@@")
as3size = len(as3.content)
print ("%s Bytes downloaded." % as3size)

print ("Uploading AS3 Extensions into BigIP...")
range = "0-{0}/{1}".format(as3size-1,as3size)
header = {"Content-Type": "application/octet-stream","Content-Range": range,"Content-Length": str(len(as3.content)),"Connection": "keep-alive"}
upload = urlreq ("https://@@{svcBigIP.address}@@:8443/mgmt/shared/file-transfer/uploads/as3.rpm",verb="POST", headers=header, params=as3.content, auth="BASIC", user="@@{admin.username}@@", passwd="@@{admin.secret}@@")
print (upload.content)

print ("Installing AS3 Extensions...")
params="{\"operation\":\"INSTALL\",\"packageFilePath\":\"/var/config/rest/downloads/as3.rpm\"}"
header={"Origin": "https://@@{svcBigIP.address}@@","Content-Type": "application/json;charset=UTF-8"}
install = urlreq("https://@@{svcBigIP.address}@@:8443/mgmt/shared/iapp/package-management-tasks", verb="POST", headers=header, params=params, auth="BASIC", user="@@{admin.username}@@", passwd="@@{admin.secret}@@")
print (install.content)
print ("Ready")