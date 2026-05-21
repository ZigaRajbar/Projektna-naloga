from pridobi_podatke import raw_podatki_s_spletne_strani
from uredi_podatke import uredi_raw_podatke, naredi_csv

stevilo_strani = 1

print(naredi_csv(uredi_raw_podatke(raw_podatki_s_spletne_strani(stevilo_strani))))
