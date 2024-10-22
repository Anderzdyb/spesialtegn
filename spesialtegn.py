import os
import re

def endre_filnavn(filnavn):
  filnavn = filnavn.replace("¾", "æ")
  filnavn = filnavn.replace("¿", "æ")
  filnavn = filnavn.replace("Œ", "å")
  filnavn = filnavn.replace("Ž", "è")
  return filnavn

def endre_filer_i_katalog(katalog):
  for rot, _, filer in os.walk(katalog):
    for fil in filer:
      gammelt_filnavn = os.path.join(rot, fil)
      nytt_filnavn = endre_filnavn(fil)
      nytt_filnavn = os.path.join(rot, nytt_filnavn)
      os.rename(gammelt_filnavn, nytt_filnavn)

# Angi katalogen hvor filene er
katalog = "e:\\saxo\\sog\\2013-Copy"
# Endre denne til din katalog
endre_filer_i_katalog(katalog)