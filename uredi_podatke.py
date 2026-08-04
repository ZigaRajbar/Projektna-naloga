import re
import csv
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

        ime_avta = re.search(
            r'<h2[^>]*>\s*([^<]+)\s*</h2>',
            podatki_oglasa,
        )

        letnik = re.search(
            r'<span>((?:19|20)\d{2})</span>',
            podatki_oglasa,
        )

        kilometrina = re.search(
            r'<span>([\d.]+)\s*km</span>',
            podatki_oglasa,
        )

        vrsta_goriva = re.search(
            r'<span>(Bencin|Dizel|Elektrika|Hibrid|Plin)</span>',
            podatki_oglasa,
        )

        menjalnik = re.search(
            r'<span>(Avtomatski|Ročni)</span>',
            podatki_oglasa,
        )

        moc_motorja = re.search(
            r'\((\d+)\s*KM\)',
            podatki_oglasa,
        )

        cena = re.search(
            r'class="(?:text-base text-gray-800 font-bold|'
            r'text-brand-800 text-2xl font-bold)">'
            r'(\d{1,3}(?:\.\d{3})*)',
            podatki_oglasa,
        )

        prodajalec = re.search(
            r'phone="[^"]+"[^>]*>\s*([^<]+)',
            podatki_oglasa,
        )

        o_avtu = {
            "Ime": ime_avta.group(1) if ime_avta else None,
            "Znamka": ime_avta.group(1).split()[0],
            "Letnik": int(letnik.group(1)) if letnik else None,
            "Prevoženi kilometri": (
                int(kilometrina.group(1).replace(".", ""))
                if kilometrina
                else "Novo vozilo"
            ),
            "Tip goriva": vrsta_goriva.group(1) if vrsta_goriva else None,
            "Tip menjalnika": menjalnik.group(1) if menjalnik else None,
            "Moč motorja": int(moc_motorja.group(1)) if moc_motorja else None,
            "Cena": int(cena.group(1).replace(".", "")) if cena else "Cena po dogovoru",
            "Prodajalec": prodajalec.group(1) if prodajalec else "Pravna oseba",
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

    with open("avti.csv", "w", encoding="utf-8", newline="") as f:
        dodaj = csv.DictWriter(f, fieldnames=stolpci)

        dodaj.writeheader()
        dodaj.writerows(podatki)

    return "Podatki uspešno urejeni!"
