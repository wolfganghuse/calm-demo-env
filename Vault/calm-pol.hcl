path "kv/data/shared/*" {
  capabilities = [ "read", "update" ]
}
path "kv/data/tenants/*" {
  capabilities = [ "read", "update" ]
}