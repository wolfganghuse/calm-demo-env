path "kv/data/tenant/{{identity.entity.id}}/*" {
capabilities = ["create", "update", "read"]
}
path "kv/delete/tenant/{{identity.entity.id}}/*" {
capabilities = ["delete", "update"]
}
path "kv/undelete/tenant/{{identity.entity.id}}/*" {
capabilities = ["update"]
}
path "kv/destroy/tenant/{{identity.entity.id}}/*" {
capabilities = ["update"]
}
path "kv/metadata/tenant/{{identity.entity.id}}/*" {
capabilities = ["list", "read", "delete"]
}
path "kv/metadata/" {
capabilities = ["list"]
}
path "kv/metadata/tenant/" {
capabilities = ["list"]
}
path "kv/data/shared/*" {
capabilities = ["read"]
}