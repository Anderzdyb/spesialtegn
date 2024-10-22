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
 -Tar en katalogbane som input.
- Bruker os.walk() for å gå gjennom alle underkataloger i den angitte katalogen.
- For hver fil:
-- Finner det gamle filnavnet.
-- Kaller endre_filnavn() for å endre filnavnet.
-- Bruker os.rename() for å endre filnavnet.

Angi katalog og kjør:
- Angi katalog til den aktuelle katalogen hvor filene er.
- Kjør endre_filer_i_katalog(katalog) for å endre filnavnene.
