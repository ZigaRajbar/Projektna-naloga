# Projektna naloga: analiza trga avtomobilov
## Avtor: Žiga Rajbar

Projektna naloga zajema in analizira oglase za avtomobile s spletne strani **DoberAvto.si**.

Program s spletne strani pridobi podatke o avtomobilih, jih uredi in shrani v datoteko CSV. Nato so podatki analizirani in grafično predstavljeni v Jupyter Notebooku.

## Zbrani podatki

Za posamezen avtomobil program poskuša pridobiti:

- ime avtomobila,
- znamko,
- letnik,
- število prevoženih kilometrov,
- vrsto goriva,
- tip menjalnika,
- moč motorja,
- ceno,
- vrsto prodajalca.

## Datoteke

- `pridobi_podatke.py` – pridobi HTML podatke s spletne strani.
- `uredi_podatke.py` – iz pridobljenih podatkov izlušči podatke o avtomobilih in jih shrani v CSV.
- `Analiza.ipynb` – vsebuje analizo podatkov in grafe.
- `podatki/avti.csv` – vsebuje urejene podatke o avtomobilih.

## Potrebne knjižnice

Za delovanje programa potrebujete naslednje knjižnice:

**requests beautifulsoup4 pandas matplotlib jupyter**

## Analiza

V notebooku so med drugim analizirani:

- povprečna cena glede na letnik,
- cena glede na prevožene kilometre,
- povprečna cena glede na znamko,
- najpogostejše znamke,
- delež različnih vrst goriva,
- delež fizičnih in pravnih prodajalcev,
- cena glede na moč motorja,
- povprečna cena glede na tip menjalnika,
- povprečna cena glede na vrsto goriva,
- povprečna cena glede na vrsto prodajalca.