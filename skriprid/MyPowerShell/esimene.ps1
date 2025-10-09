<#
Siia vabalt mitmerealine kommentaar
#>

# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
Clear-Host #Puhasta ekraan
Get-Date #Näita tänast kuupäeva

$username = Read-Host -Prompt "Sisesta enda kasutajanimi"

if($username -eq $env:USERNAME){
    Write-Host "Õige kasutajanimi"
} else {
     Write-Host "Vale kasutajanimi $username, eeldati $env:USERNAME "
}
[int]$year = Read-Host "Sisest Aasta"
if($year -eq (Get-Date).Year){
    Write-Host "Käesolev Aasta"
} Else{
    Write-Host "mõni teine aasta : $year"
}