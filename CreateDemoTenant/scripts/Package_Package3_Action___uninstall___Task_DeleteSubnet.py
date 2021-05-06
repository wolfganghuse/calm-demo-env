headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

# Set the address and make cluster/list call
url = "https://@@{PrismCentralDemo.address}@@:9440/api/nutanix/v3/subnets/@@{subnet_uuid}@@"
resp = urlreq(url, verb='DELETE', user="@@{cred_PCDemo.username}@@", passwd="@@{cred_PCDemo.secret}@@", auth='BASIC', headers=headers, verify=False)

# If the call went through successfully, check the progress
if resp.ok:
    print "task_uuid={0}".format(json.loads(resp.content)['status']['execution_context']['task_uuid'])

# If the call failed
else:
        print("Call failed"), json.dumps(json.loads(resp.content), indent=4)
        exit(1)
