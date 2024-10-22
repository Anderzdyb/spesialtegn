# spesialtegn
søk/bytt spesialtegn
Forklaring:

Importer nødvendige biblioteker:

os for filoperasjonerog re for regulære uttrykk (brukbar for mer komplekse søk og bytt).

endre_filnavn(filnavn)-funksjonen:
- Tar et filnavn som input.
- Bruker replace() for å bytte ut hvert spesialtegn med den tilsvarende bokstaven.
- Returnerer det oppdaterte filnavnet.

endre_filer_i_katalog(katalog)-funksjonen:
- Tar en katalogbane som input.
- Bruker os.walk() for å gå gjennom alle underkataloger i den angitte katalogen.
- For hver fil:
-- Finner det gamle filnavnet.
-- Kaller endre_filnavn() for å endre filnavnet.
-- Bruker os.rename() for å endre filnavnet.

Angi katalog og kjør:
- Angi katalog til den aktuelle katalogen hvor filene er.
- Kjør endre_filer_i_katalog(katalog) for å endre filnavnene.

  Alterntativ for Windows Powershell
Angi katalog: Definerer variabelen $katalog til den aktuelle katalogen.
Hent filer: Get-ChildItem henter alle filer i katalogen, inkludert underkataloger, ved bruk av -Recurse.
Sløyfe gjennom filer: ForEach-Object går gjennom hver fil.
Bytt ut tegn: $_.Name -replace "¾", "æ" -replace "¿", "æ" -replace "Œ", "å" bruker -replace for å bytte ut spesialtegnene.
Sett sammen ny filbane: Join-Path $katalog.Parent $nyttNavn setter sammen den nye filbanen ved å bruke den oppdaterte filnavnet og den opprinnelige katalogen.
Endre filnavn: Rename-Item endrer filnavnet til det nye filnavnet.
