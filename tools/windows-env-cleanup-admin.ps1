$ErrorActionPreference = "Stop"

$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$backupRoot = "E:\Applications\_cleanup-backup\$stamp-admin"
New-Item -ItemType Directory -Force -Path $backupRoot | Out-Null

reg export "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" "$backupRoot\HKLM-Environment-before-admin-clean.reg" /y | Out-Null
reg export "HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall\{7C40E3FE-8918-49C8-95D4-F6BF883C74DF}" "$backupRoot\HKLM-CMake-Uninstall-before-remove.reg" /y 2>$null | Out-Null

$removeMachinePath = @(
  "E:\min",
  "w64\bin",
  "E:\Gpg4win\..\GnuPG\bin",
  "E:\CMake\bin"
)

$machineRaw = [Environment]::GetEnvironmentVariable("Path", "Machine")
$kept = New-Object System.Collections.Generic.List[string]
$removed = New-Object System.Collections.Generic.List[string]

foreach ($entry in ($machineRaw -split ";" | Where-Object { $_ -and $_.Trim() })) {
  $trim = $entry.Trim()
  $normalized = $trim.TrimEnd("\").ToLowerInvariant()
  $shouldRemove = $false

  foreach ($candidate in $removeMachinePath) {
    if ($normalized -eq $candidate.TrimEnd("\").ToLowerInvariant()) {
      $shouldRemove = $true
      break
    }
  }

  if ($shouldRemove) {
    $removed.Add($trim)
  } else {
    $kept.Add($trim)
  }
}

[Environment]::SetEnvironmentVariable("Path", ($kept -join ";"), "Machine")

$cmakeKey = "HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\{7C40E3FE-8918-49C8-95D4-F6BF883C74DF}"
$cmakeRemoved = $false
if (Test-Path $cmakeKey) {
  $cmake = Get-ItemProperty $cmakeKey
  $installLocation = ($cmake.InstallLocation -as [string]).Trim('"')
  if ($cmake.DisplayName -eq "CMake" -and $installLocation -eq "E:\CMake\" -and -not (Test-Path -LiteralPath $installLocation)) {
    Remove-Item -LiteralPath $cmakeKey -Force
    $cmakeRemoved = $true
  }
}

$emptyStartFolders = @(
  "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Texas Instruments\Code Composer Studio",
  "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\cpolar",
  "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\CCS 20.5.0.00028"
)

$removedFolders = New-Object System.Collections.Generic.List[string]
foreach ($folder in $emptyStartFolders) {
  if (Test-Path -LiteralPath $folder) {
    $hasItems = Get-ChildItem -LiteralPath $folder -Force -ErrorAction SilentlyContinue | Select-Object -First 1
    if (-not $hasItems) {
      Remove-Item -LiteralPath $folder -Force
      $removedFolders.Add($folder)
    }
  }
}

[PSCustomObject]@{
  BackupRoot = $backupRoot
  RemovedMachinePath = $removed
  CMakeUninstallKeyRemoved = $cmakeRemoved
  RemovedEmptyStartFolders = $removedFolders
} | Format-List
