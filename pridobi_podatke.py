import requests
import time


def raw_podatki_s_spletne_strani(stevilo_strani):
    vsi_podatki = ""
    for i in range(1, stevilo_strani + 1):
        r = requests.get(f"https://www.doberavto.si/iskanje?page={i}")

        if r.status_code != 200:
            return f"Napaka na strani {i}."

        vsi_podatki += r.text
        time.sleep(2)
    return vsi_podatki
