path "kv/data/tenants/mandant1/*" {
capabilities = ["create", "update", "read"]
}
path "kv/delete/tenants/mandant1/*" {
capabilities = ["delete", "update"]
}
path "kv/undelete/tenants/mandant1/*" {
capabilities = ["update"]
}
path "kv/destroy/tenants/mandant1/*" {
capabilities = ["update"]
}
path "kv/metadata/users/mandant1/*" {
capabilities = ["list", "read", "delete"]
}
path "kv/metadata/" {
capabilities = ["list"]
}
path "kv/metadata/tenants/" {
capabilities = ["list"]
}
path "kv/data/shared/*" {
capabilities = ["read"]
}