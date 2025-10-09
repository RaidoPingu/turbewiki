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


#Masiiv
$nums = @() #Tühi masiiv
$nums += 5
$nums += 2
$nums += 6
$nums += Get-Random -Minimum 1 -Maximum 10

Write-Host $nums # Väljastab masiivi
Write-Host $nums[-1] #Võtab viimase numberi masiivist
Write-Host $nums[$nums.Length-1] #Võtab samuti viimase numbri masiivist
$num = 0 # Algväärtustamine
$num += 5
$num += 3
$num += Get-Random -Minimum 1 -Maximum 10

Write-Host $num


<# 
Liida kokku 2 juhuslikku numbrit. Mõlemad vahemikus 1-10 .
Vastus on muutujas  $random
#>

$random = 0
$random1 = Get-Random -Minimum 1 -Maximum 10 
Write-Host $random1
$random2 = Get-Random -Minimum 1 -Maximum 10
Write-Host $random2
$random = $random1 + $random2

Write-Host $random
# Sama asi:
$random = (Get-Random -Minimum 1 -Maximum 10) + (Get-Random -Minimum 1 -Maximum 10)

Write-Host $random

