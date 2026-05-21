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
            r'class="order-2 line-clamp-2 text-lg font-bold text-gray-950">(\w+[\s\w\s\w]*)',
            podatki_oglasa,
        )
        letnik = re.search(
            r'style="font-size:16px;"></span><span>(\d{4})',
            podatki_oglasa,
        )
        kilometrina = re.search(r"([\d.]+\skm)", podatki_oglasa)
        vrsta_gorivca = re.search(
            r'style="font-size:16px;"></span><span>(\w{5}[\s\w]*)',
            podatki_oglasa,
        )
        menjalnik = re.search(
            r"i-posting:auto-transmission.*?</span>\s*<span>(.*?)</span>",
            podatki_oglasa,
        )
        moc_motorja = re.search(
            r"i-posting:zap.*?</span>\s*<span>\d+\w+\s\((\d+)\)", podatki_oglasa
        )
        cena = re.search(
            r'class="text-base\stext-gray-800\sfont-bold">(\d+[.\d]*)', podatki_oglasa
        )

        o_avtu = {
            "Ime": ime_avta.group(1) if ime_avta else None,
            "Znamka": ime_avta.group(1).split()[0],
            "Letnik": letnik.group(1) if letnik else None,
            "Prevoženi kilometri": (
                kilometrina.group(1) if kilometrina else "Novo vozilo"
            ),
            "Tip goriva": vrsta_gorivca.group(1) if vrsta_gorivca else None,
            "Tip menjalnika": menjalnik.group(1) if menjalnik else None,
            "Moč motorja": moc_motorja.group(1) + "KM" if moc_motorja else None,
            "Cena": cena.group(1) + " €" if cena else "Cena po dogovoru",
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
    ]

    with open("Avti.csv", "w", encoding="utf-8", newline="") as f:
        dodaj = csv.DictWriter(f, fieldnames=stolpci)

        dodaj.writeheader()
        dodaj.writerows(podatki)
