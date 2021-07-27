Write-Host "`n===================================================="
write-Host "Delete OU for customer @@{tenant_prefix}@@"
Remove-ADOrganizationalUnit -Identity "@@{Distinguished_Name}@@" -Recursive -Confirm:$False

exit 0
