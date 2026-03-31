"""VARIANT 2 (LÜHIKE): ILMAJAAMA ANDMETE ANALÜÜS

ÜLESANDE KIRJELDUS:
Ilmajaam vajab lihtsat programmi ilmaandmete analüüsimiseks.

SISENDANDMED:
Fail "ilm.txt" sisaldab ilmavaatluste andmeid formaaadis:
Kuupäev;Temperatuur;Sademed

Näiteks:
2024-01-01;-5.2;2.3
2024-01-02;-3.8;0.0
2024-01-03;1.5;5.1

Kus:
- Kuupäev (AAAA-KK-PP)
- Temperatuur (°C, võib olla negatiivne)
- Sademed (mm, 0 kui ei sada)

ÜLESANDED:

1. Loe fail sisse ja salvesta andmed järjendisse (iga päev on sõnastik).

2. Kuva menüü järgmiste valikutega:
   1 - Kuva kõik mõõtmised
   2 - Temperatuuri statistika
   3 - Sademete analüüs
   4 - Salvesta kokkuvõte
   0 - Välju

3. KUVA KÕIK MÕÕTMISED: Prindi välja kõik ilmavaatlused tabelina.

4. TEMPERATUURI STATISTIKA:
   - Arvuta keskmine temperatuur
   - Leia kõrgeim ja madalaim temperatuur (koos kuupäevaga)
   - Loe kokku päevi üle 0°C
   - Kuva kõik tulemused

5. SADEMETE ANALÜÜS:
   - Arvuta kogu sademete hulk
   - Leia päev kõige rohkemate sademetega
   - Loe kokku päevi ilma sademeteta (sademed = 0)
   - Kuva tulemused

6. SALVESTA KOKKUVÕTE: Loo fail "ilm_kokkuvõte.txt", kuhu kirjuta:
   - Mõõtmiste arv
   - Keskmine temperatuur
   - Kogu sademete hulk
   - Kõige külmem päev
   - Kõige soojem päev

7. Programm peab töötama tsüklis kuni kasutaja valib "0 - Välju"

HINDAMISKRITEERIUMID:
- Failist lugemine (20p)
- Menüü ja kasutajaliides (15p)
- Temperatuuri statistika (30p)
- Sademete analüüs (20p)
- Kokkuvõtte salvestamine (10p)
- Koodi loetavus (5p)

KOKKU: 100 punkti
Ajakulu: ~30 minutit
"""
def read_data(filename):
    result = []
    with open(filename, "r") as f:
        for line in f:
            line = line.rstrip("\n")
            result.append(line)
    return result

def menu_choices():





if __name__ == '__main__':

