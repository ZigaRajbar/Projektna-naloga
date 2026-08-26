from pridobi_podatke import raw_podatki_s_spletne_strani
from uredi_podatke import uredi_raw_podatke, naredi_csv


def main():
    stevilo_strani = 200

    print("Pridobivanje podatkov...")
    raw_podatki = raw_podatki_s_spletne_strani(stevilo_strani)

    print("Urejanje podatkov...")
    urejeni_podatki = uredi_raw_podatke(raw_podatki)

    print(f"Najdenih avtomobilov: {len(urejeni_podatki)}")

    naredi_csv(urejeni_podatki)
    print("Podatki uspešno urejeni!")


main()
