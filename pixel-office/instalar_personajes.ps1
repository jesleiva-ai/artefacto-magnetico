# Respalda los personajes de fábrica de Pixel Agents y los reemplaza por los neón.
# Uso (desde esta carpeta):  powershell -ExecutionPolicy Bypass -File .\instalar_personajes.ps1
# Requisito: haber corrido "npx pixel-agents" al menos una vez (para que exista el caché).

$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$nuevos = Join-Path $here "assets\characters"
$backupRoot = Join-Path $HOME "pixel-office-backup"

# Busca todas las carpetas de personajes del paquete dentro del caché de npx
# (dist\assets\characters y dist\webview\assets\characters).
$destinos = Get-ChildItem -Path "$env:LOCALAPPDATA\npm-cache\_npx" -Recurse -Filter "char_0.png" -ErrorAction SilentlyContinue |
    Where-Object { $_.DirectoryName -like "*node_modules\pixel-agents\dist*\characters" } |
    ForEach-Object { $_.DirectoryName } | Sort-Object -Unique

if (-not $destinos) { throw "No encontré pixel-agents en el caché de npx. Corré 'npx pixel-agents' una vez y volvé a intentar." }

$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$i = 0
foreach ($dir in $destinos) {
    $backup = Join-Path $backupRoot "$stamp\$i"
    New-Item -ItemType Directory -Force -Path $backup | Out-Null
    Copy-Item (Join-Path $dir "char_*.png") $backup
    Set-Content -Path (Join-Path $backup "ORIGEN.txt") -Value $dir
    Copy-Item (Join-Path $nuevos "char_*.png") $dir -Force
    Write-Host "Parcheado: $dir"
    Write-Host "  Respaldo: $backup"
    $i++
}
Write-Host ""
Write-Host "Listo. Reiniciá el servidor (Ctrl+C y 'npx pixel-agents' de nuevo) y recargá el navegador."
Write-Host "OJO: el parche se pierde si se limpia el caché de npx o se actualiza pixel-agents. Volvé a correr este script."
