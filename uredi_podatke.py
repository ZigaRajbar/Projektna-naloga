import re
from bs4 import BeautifulSoup


def uredi_raw_podatke(podatki):
    podatki_o_avtih = []

    soup = BeautifulSoup(podatki, "html.parser")

    avti = soup.find_all(
        "div",
        class_="relative flex min-h-136.5 w-full flex-col rounded-lg border border-gray-200 pt-52.5 transition-shadow duration-150 group-hover/carousel:shadow-none! hover:shadow-md bg-white",
    )

    for avto in avti:

        ime_avta = re.search(
            r'class="order-2 line-clamp-2 text-lg font-bold text-gray-950">(\w+[\s\w\s\w]*)',
            str(avto),
        )
        letnik = re.search(r"(\d{4})", str(avto))
        kilometrina = re.search(r"([\d.]+\s*km)", str(avto))
        vrsta_gorivca = re.search(
            r'style="font-size:16px;"></span><span>(\w{5}[\s\w]*)',
            str(avto),
        )
        menjalnik = re.search(
            r"i-posting:auto-transmission.*?</span>\s*<span>(.*?)</span>",
            str(avto),
        )
        moc_motorja = re.search(
            r"i-posting:zap.*?</span>\s*<span>\d+\w+\s\((\d+\w+)\)", str(avto)
        )

        o_avtu = {
            "Ime": ime_avta.group(1) if ime_avta else None,
            "Letnik": letnik.group(1) if letnik else None,
            "Prevoženi kilometri": kilometrina.group(1) if kilometrina else None,
            "Tip goriva": vrsta_gorivca.group(1) if vrsta_gorivca else None,
            "Tip menjalnika": menjalnik.group(1) if menjalnik else None,
            "Moč motorja": moc_motorja.group(1) if moc_motorja else None,
        }

        podatki_o_avtih.append(o_avtu)

    print(len(podatki_o_avtih))
    return podatki_o_avtih
