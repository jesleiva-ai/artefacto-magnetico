# Restaura los personajes de fábrica desde el respaldo más antiguo (el primero que se hizo).
# Uso:  powershell -ExecutionPolicy Bypass -File .\restaurar_personajes.ps1

$ErrorActionPreference = "Stop"
$backupRoot = Join-Path $HOME "pixel-office-backup"
$primero = Get-ChildItem $backupRoot -Directory | Sort-Object Name | Select-Object -First 1
if (-not $primero) { throw "No hay respaldos en $backupRoot" }

foreach ($b in Get-ChildItem $primero.FullName -Directory) {
    $destino = (Get-Content (Join-Path $b.FullName "ORIGEN.txt")).Trim()
    if (Test-Path $destino) {
        Copy-Item (Join-Path $b.FullName "char_*.png") $destino -Force
        Write-Host "Restaurado: $destino"
    } else {
        Write-Host "Ya no existe (caché limpiado): $destino"
    }
}
Write-Host "Reiniciá el servidor para ver los personajes de fábrica."
