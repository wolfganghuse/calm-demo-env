#script
DOMAIN = '@@{DOMAIN}@@'
ROOT_OU = '@@{ROOT_OU}@@'

# convert domain name to Microsoft AD path
# -----------------------------------------------------------
def convert_domain_to_ad_path(domain, root_ou):
    path = ''
    if domain[len(domain)-1:] != '.':
        domain = domain + '.'
    
    while domain.find('.') >= 0:
        x = domain.find('.')
        path = path + ',DC={}'.format(domain[:x])
        domain = domain[x+1:]
    
    return '{},{}'.format(root_ou, path[1:])

ad_path = convert_domain_to_ad_path(DOMAIN, ROOT_OU)

print('AD_PATH=OU={}'.format(ad_path))
