<#
Äraarvamis emäng. Numbrid 1-100
Tagauks
Mäng on läbi Küsitakse nime ja koos käikude ja sammudega
Kirjutatakse faili
#>
$pc_nr = Get-Random -Minimum 1 -Maximum 100
[System.Boolean]$game_over = $false
$Global:steps = 0 #Globaalne muutuja sammud
$filename = Join-Path -Path $PSScriptRoot -ChildPath "result.txt"
Write-Host $pc_nr $filename # Kontrolliks

function writeToFile{
    $name = Read-Host "Mängija nimi"
    ($name, $Global:steps -join ";") | Out-File -FilePath $filename -Append
}



#writeToFile
