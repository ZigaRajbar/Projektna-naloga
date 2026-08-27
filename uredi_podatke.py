import csv
import re
import os
from bs4 import BeautifulSoup


def uredi_raw_podatke(podatki):
    podatki_o_avtih = []
    soup = BeautifulSoup(podatki, "html.parser")

    avti = soup.find_all(
        "div",
        class_="relative flex min-h-136.5 w-full flex-col rounded-lg border border-gray-200 pt-52.5 transition-shadow duration-150 group-hover/carousel:shadow-none! hover:shadow-md bg-white",
    )

    for avto in avti:
        podatki_oglasa = str(avto)

        ime_avta = re.search(r"<h2.*?>(.*?)</h2>", podatki_oglasa)
        letnik = re.search(r">(19\d\d|20\d\d)<", podatki_oglasa)
        kilometrina = re.search(r">([\d.]+) km<", podatki_oglasa)
        vrsta_goriva = re.search(
            r">(Bencin|Dizel|Električni pogon|Hibrid|Plin)<", podatki_oglasa
        )
        menjalnik = re.search(r">(Avtomatski|Ročni)<", podatki_oglasa)
        moc_motorja = re.search(r"\((\d+)KM\)", podatki_oglasa)
        cena = re.search(
            r'class="(?:text-base text-gray-800 font-bold|text-brand-800 text-2xl font-bold)">\s*(\d{1,3}(?:\.\d{3})*)',
            podatki_oglasa,
        )

        if ime_avta:
            ime = ime_avta.group(1).strip()
            znamka = ime.split()[0]
        else:
            ime = None
            znamka = None

        if cena:
            cena_avta = int(cena.group(1).replace(".", ""))
        elif "Cena po dogovoru" in podatki_oglasa:
            cena_avta = "Cena po dogovoru"
        else:
            cena_avta = None

        if "Fizična oseba" in podatki_oglasa:
            prodajalec = "Fizična oseba"
        else:
            prodajalec = "Pravna oseba"

        o_avtu = {
            "Ime": ime,
            "Znamka": znamka,
            "Letnik": int(letnik.group(1)) if letnik else None,
            "Prevoženi kilometri": (
                int(kilometrina.group(1).replace(".", "")) if kilometrina else None
            ),
            "Tip goriva": vrsta_goriva.group(1) if vrsta_goriva else None,
            "Tip menjalnika": menjalnik.group(1) if menjalnik else None,
            "Moč motorja": int(moc_motorja.group(1)) if moc_motorja else None,
            "Cena": cena_avta,
            "Prodajalec": prodajalec,
        }

        podatki_o_avtih.append(o_avtu)

    return podatki_o_avtih


def naredi_csv(podatki):
    stolpci = [
        "Ime",
        "Znamka",
        "Letnik",
        "Prevoženi kilometri",
        "Tip goriva",
        "Tip menjalnika",
        "Moč motorja",
        "Cena",
        "Prodajalec",
    ]

    os.makedirs("podatki", exist_ok=True)

    with open("podatki/avti.csv", "w", encoding="utf-8", newline="") as datoteka:

        dodaj = csv.DictWriter(datoteka, fieldnames=stolpci)
        dodaj.writeheader()
        dodaj.writerows(podatki)
