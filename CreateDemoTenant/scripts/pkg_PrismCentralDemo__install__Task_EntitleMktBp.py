username = "@@{cred_PCDemo.username}@@"
username_secret = "@@{cred_PCDemo.secret}@@"
pc_address = "@@{address}@@"

MARKET_PREFIX = '{"values": ["CST"]}'
projUuid = '@@{PROJECT_UUID}@@'
projName = '@@{project_name}@@'

# api call function
# ================================================================
def http_request(api_endpoint, payload='', method='POST'):
  headers = {
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  }


  url = "https://localhost:9440{}".format(api_endpoint)

  
  if len(payload) > 0:
      payload = json.dumps(payload)
      
  
  resp = urlreq(
      url,
      verb=method,
      params=payload,
      auth='BASIC', user="@@{cred_PCDemo.username}@@", passwd="@@{cred_PCDemo.secret}@@",
      headers=headers,
      verify=False
  )
  
  if resp.ok:
      return json.loads(resp.content)
  else:
      print('Error in API call')
      exit(1)


# get list of published items
# ================================================================
def get_published_items(MARKET_PREFIX):
  api_url = '/api/nutanix/v3/groups'
  payload = {}
  payload['filter_criteria'] = 'marketplace_item_type_list==APP;(app_state==PUBLISHED)'
  payload['entity_type'] = 'marketplace_item'
  payload['group_member_attributes'] = [{'attribute': 'name'}]
  
  # load list of visible variables
  prefix_list = json.loads(MARKET_PREFIX)['values']
  
  result = http_request(api_url, payload=payload)
  
  published_list = []
  for entity_item in result['group_results'][0]['entity_results']:
    blueprint_name = ''
    # check for name field
    for field in entity_item['data']:
      if field.get('name', None) == 'name':
        blueprint_name = field['values'][0]['values'][0]
        
    # check if the blueprint name is in the prefix list
    if blueprint_name[0] == '_':
      blueprint_prefix = blueprint_name[1:blueprint_name.find('_', 1)]
      if blueprint_prefix in prefix_list:
          published_list.append({ 'uuid': entity_item['entity_id'],
                                  'name': blueprint_name,
                                  'display_name': blueprint_name[blueprint_name.find('_', 1)+1:],
                                  'category': blueprint_prefix })

  return published_list


# publish blueprint to project
# ================================================================
def publish_blueprint(blueprint_uuid, project_uuid, project_name):
  api_endpoint = '/api/nutanix/v3/calm_marketplace_items/{}'.format(blueprint_uuid)
  blueprint = http_request(api_endpoint, method='GET')
  payload = {}
  if blueprint['spec']['resources']:
    payload['spec'] = blueprint['spec']
    payload['metadata'] = blueprint['metadata']
    payload['api_version'] = '3.0'
    payload['spec']['resources']['project_reference_list'].append(
      { 'kind': 'project',
        'name': project_name,
        'uuid': project_uuid })
    
  
  api_endpoint = '/api/nutanix/v3/calm_marketplace_items/{}'.format(blueprint_uuid)
  result = http_request(api_endpoint, payload=payload, method='PUT')
  
  if result:
    return True
  else:
    return False
  


# ================================================================
# ================================================================
# ================================================================

# main run function
published_blueprints = get_published_items(MARKET_PREFIX)

for blueprint in published_blueprints:
    update_result = publish_blueprint(blueprint['uuid'], projUuid, projName)
    if update_result:
        print('Blueprint: "{}" added to project "{}"'.format(blueprint['name'], projName))