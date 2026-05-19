import requests
from bs4 import BeautifulSoup
import re
import csv


def podatki_s_spletne_strani(st_strani):
    niz_avtov = []

    for i in range(1, st_strani + 1):
        r = requests.get(f"https://www.doberavto.si/iskanje?page={i}")

        if r.status_code != 200:
            return f"Napaka na strani {i}."

        soup = BeautifulSoup(r.text, "html.parser")
        oglasi = soup.find_all(
            "div",
            class_="relative flex min-h-136.5 w-full flex-col rounded-lg border border-gray-200 pt-52.5 transition-shadow duration-150 group-hover/carousel:shadow-none! hover:shadow-md bg-white",
        )
        print(oglasi)
        for oglas in oglasi:
            ime = oglas.select_one(
                "h2", class_="order-2 line-clamp-2 text-lg font-bold text-gray-950"
            )
            cena = oglas.select_one(
                "div", class_="text-base font-bold text-gray-800 line-through"
            )

            podatki = {
                "Ime": ime.get_text(strip=True),
                "Cena": cena.get_text(strip=True),
            }
            niz_avtov.append(podatki)

    print(niz_avtov)
    print(len(niz_avtov))

    return niz_avtov


print(podatki_s_spletne_strani(1))
