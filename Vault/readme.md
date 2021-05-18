VAULT_TOKEN="s.ZeyandfQGwM61TsZeczUIOe0"
export VAULT_ADDR="http://172.23.131.187:8200"

vault policy write admin admin-policy.hcl

vault write auth/token/roles/admin allowed_policies=admin orphan=true

vault token create -display-name=admin-1 -role=admin

vault policy write tenant tenant-policy.hcl

vault token create -display-name=demo1 -policy=tenant