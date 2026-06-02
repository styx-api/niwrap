#!/usr/bin/env pwsh
#
# Dump MRtrix3 command metadata for every version in versions.json.
#
# For each version V it builds the Dockerfile with --build-arg MRTRIX_VERSION=V
# and exports the raw JSON dump to dump/V/{cpp,python}/.
#
# Requires: docker (with buildx).
#
# Usage:
#   ./extract.ps1                 # all versions in versions.json
#   ./extract.ps1 3.0.4 3.0.5     # explicit versions, ignoring versions.json

[CmdletBinding()]
param([Parameter(ValueFromRemainingArguments = $true)] [string[]] $Versions)

$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path

if (-not $Versions) {
    $Versions = Get-Content (Join-Path $here "versions.json") -Raw | ConvertFrom-Json
}

$env:DOCKER_BUILDKIT = "1"
foreach ($v in $Versions) {
    Write-Host "==> Dumping MRtrix3 $v"
    docker buildx build `
        --build-arg "MRTRIX_VERSION=$v" `
        --target artifact `
        --output "type=local,dest=$here/dump/$v" `
        $here
    if ($LASTEXITCODE -ne 0) { throw "docker build failed for MRtrix3 $v" }
    Write-Host "    -> $here/dump/$v"
}
