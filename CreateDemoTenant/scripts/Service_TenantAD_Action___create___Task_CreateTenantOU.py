Write-Host "`n===================================================="
write-Host "Create OU for new customer"
New-ADOrganizationalUnit -Name "@@{tenant_prefix}@@" -Path "@@{AD_PATH}@@" -ProtectedFromAccidentalDeletion $False -PassThru

Write-Host "`n===================================================="
write-Host "Create new customer owner account"
New-ADUser `
 -Name "@@{FIRST_NAME}@@ @@{LAST_NAME}@@" `
 -GivenName "@@{FIRST_NAME}@@" `
 -Surname "@@{LAST_NAME}@@" `
 -SamAccountName "@@{USERID}@@" `
 -UserPrincipalName "@@{USERID}@@@@@{DOMAIN}@@" `
 -Path "OU=@@{tenant_prefix}@@,@@{AD_PATH}@@" `
 -AccountPassword(ConvertTo-SecureString -asPlainText -Force -String "@@{PASSWORD}@@") `
 -Description "@@{tenant_prefix}@@" `
 -Company "@@{tenant_prefix}@@" `
 -Enabled $True -PassThru
 
Write-Host "`n===================================================="
write-Host "Create Admins group for the new customer"
 New-ADGroup `
  -Name "@@{tenant_prefix}@@-ADMIN" `
  -SamAccountName "@@{tenant_prefix}@@-ADMIN" `
  -GroupCategory Security -GroupScope Global `
  -DisplayName "@@{tenant_prefix}@@ - Admins" `
  -Path "OU=@@{tenant_prefix}@@,@@{AD_PATH}@@" `
  -PassThru


Write-Host "`n===================================================="
write-Host "add the user to projecgt admin group"
Add-ADGroupMember `
 -Identity "@@{tenant_prefix}@@-ADMIN" `
 -Members "@@{USERID}@@" `
 -PassThru


Write-Host "`n===================================================="
write-Host "Create Operators group for the new customer"
 New-ADGroup `
  -Name "@@{tenant_prefix}@@-OPERATOR" `
  -SamAccountName "@@{tenant_prefix}@@-OPERATOR" `
  -GroupCategory Security -GroupScope Global `
  -DisplayName "@@{tenant_prefix}@@ - Operators" `
  -Path "OU=@@{tenant_prefix}@@,@@{AD_PATH}@@" `
  -PassThru

exit 0
