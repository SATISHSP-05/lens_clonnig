$ErrorActionPreference = "Stop"

$version = "5.3.3"
$baseUrl = "https://cdn.jsdelivr.net/npm/bootstrap@$version/dist"
$dest = Join-Path $PSScriptRoot "..\\backend\\static\\vendor\\bootstrap"

New-Item -ItemType Directory -Force -Path $dest | Out-Null

Invoke-WebRequest -Uri "$baseUrl/css/bootstrap.min.css" -OutFile (Join-Path $dest "bootstrap.min.css")
Invoke-WebRequest -Uri "$baseUrl/js/bootstrap.bundle.min.js" -OutFile (Join-Path $dest "bootstrap.bundle.min.js")

Write-Host "Downloaded Bootstrap $version to $dest"
