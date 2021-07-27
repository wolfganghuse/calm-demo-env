#script
projectUuid = "@@{project_name}@@"
envuuid = "@@{PROJECT_UUID}@@"
username = "@@{cred_PCDemo.username}@@"
username_secret = "@@{cred_PCDemo.secret}@@"
AD_PATH = "@@{TenantAD.AD_PATH}@@"
Distinguished_Nme = "@@{TenantAD.Distinguished_Name}@@"
ROLE_ADMIN_UUID = "@@{ROLE_ADMIN_UUID}@@"
ROLE_OPERATOR_UUID = "@@{ROLE_OPERATOR_UUID}@@"
GROUP_ADMIN_UUID = "@@{GROUP_ADMIN_UUID}@@"
GROUP_OPERATOR_UUID = "@@{GROUP_OPERATOR_UUID}@@"

api_server = "@@{address}@@"
api_server_port = "9440"
api_server_endpoint = "/api/nutanix/v3/projects_internal/{}".format(envuuid)

length = 100
url = "https://{}:{}{}".format(
    api_server,
    api_server_port,
    api_server_endpoint
)

method = "GET"
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}


#region make the api call
print("Making a {} API call to {}".format(method, url))
r = urlreq(
    url,
    verb=method,
    auth='BASIC',
    user=username,
    passwd=username_secret,
    headers=headers,
    verify=False
)
# endregion
if r.ok:
    resp = json.loads(r.content)
    payload = resp

else:
    print("Post request failed", r.content)
    exit(1)

def entity_collection_list(entities_all, entities_self):

    default_list = []
    for entity in entities_all:
        default_list.append({
            'operator': 'IN',
            'left_hand_side': {'entity_type': entity},
            'right_hand_side': {'collection': 'ALL'}
        })

    for entity in entities_self:
        default_list.append({
            'operator': 'IN',
            'left_hand_side': {'entity_type': entity},
            'right_hand_side': {'collection': 'SELF_OWNED'}
        })

    return default_list

def generate_filter_list(project_uuid, admin=True):
    acl = []
    acl.append({
        'scope_filter_expression_list': [
            {
                'operator': 'IN',
                'left_hand_side': 'PROJECT',
                'right_hand_side': {'uuid_list': [project_uuid]}
            }
        ],
        'entity_filter_expression_list': [
            {
                'operator': 'IN',
                'left_hand_side': {'entity_type': 'ALL'},
                'right_hand_side': {'collection': 'ALL'}
            }
        ]
    })

    if admin:
        entities_all=['image', 'app_icon', 'category']
        entities_self=['marketplace_item', 'app_task', 'app_variable']
    else:
        entities_all=['app_icon', 'category']
        entities_self=[]

    acl.append({
    'entity_filter_expression_list':entity_collection_list(entities_all, 
                                                           entities_self)})
    return acl
    
filter_list_admin = generate_filter_list(envuuid)
filter_list_operator = generate_filter_list(envuuid, False)

admin_group = {
    'kind': 'user_group',
    'name': 'CN={}-ADMIN,OU={},{}'.format(projectUuid, projectUuid, AD_PATH),
    'uuid': GROUP_ADMIN_UUID
}

operator_group = {
    'kind': 'user_group',
    'name': 'CN={}-OPERATOR,OU={},{}'.format(projectUuid, projectUuid, AD_PATH),
    'uuid': GROUP_OPERATOR_UUID
}

acp_admin = {
    'acp': {
        'name': 'ACP-TENANT-{}'.format(projectUuid),
        'resources': {
            'role_reference': {
                'kind': 'role',
                'uuid': ROLE_ADMIN_UUID
            },
                'user_group_reference_list': [admin_group],
                'user_reference_list': [],
                'filter_list': {'context_list': filter_list_admin}
            },
            'description': 'Admin role for {}'.format(projectUuid)
        },
        'metadata': {
            'kind': 'access_control_policy'
        },
        'operation': 'ADD'
    }

acp_operator = {
    'acp': {
        'name': 'ACP-TENANT-{}'.format(projectUuid),
        'resources': {
                'role_reference': {
                    'kind': 'role',
                    'uuid': ROLE_OPERATOR_UUID
                },
                'user_group_reference_list': [operator_group],
                'user_reference_list': [],
                'filter_list': {'context_list': filter_list_operator}
            },
            'description': 'Operator role for {}'.format(projectUuid)
        },
        'metadata': {
            'kind': 'access_control_policy'
        },
        'operation': 'ADD'
}

access_control_policy_list = [acp_admin, acp_operator]

environment = {
    "kind": "environment",
    "uuid": "@@{ENV_UUID}@@"
}
del payload['status']
payload['spec']['project_detail']['resources']['environment_reference_list'] = []
payload['spec']['project_detail']['resources']['environment_reference_list'].append(environment)

payload['spec']['project_detail']['resources']['external_user_group_reference_list'] = [admin_group, operator_group]
#payload['spec']['resources']['external_user_group_reference_list'].append()

payload['spec']['access_control_policy_list'] = access_control_policy_list

print payload
method = "PUT"

#region make the api call
print("Making a {} API call to {}".format(method, url))
r = urlreq(
    url,
    verb=method,
    auth='BASIC',
    user=username,
    passwd=username_secret,
    params=json.dumps(payload),
    headers=headers,
    verify=False
)
# endregion
if r.ok:
    exit(0)

else:
    print("Post request failed", r.content)
    exit(1)
