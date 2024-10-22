$katalog = "C:\path\to\files" # Endre denne til din katalog

Get-ChildItem -Path $katalog -Recurse | ForEach-Object {
  $gammeltNavn = $_.FullName
  $nyttNavn = $_.Name -replace "¾", "æ" -replace "¿", "æ" -replace "Œ", "å"
  $nyttNavn = Join-Path $katalog.Parent $nyttNavn
  Rename-Item -Path $gammeltNavn -NewName $nyttNavn
}