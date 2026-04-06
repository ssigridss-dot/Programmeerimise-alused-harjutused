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
def read_data(filename: str) -> list:
    data = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(";")

            date = parts[0]
            temp = float(parts[1])
            rain = float(parts[2])

            day = {
                "date": date,
                "temperature": temp,
                "rain": rain
            }

            data.append(day)

    return data


def show_all(data: list) -> None:
    print("\nKuupäev     | Temp (°C) | Sademed (mm)")
    print("-" * 40)

    for day in data:
        print(day["date"], "|", day["temperature"], "|", day["rain"])


def temperature_stats(data: list) -> None:
    total_temp = 0
    count = 0

    max_temp = data[0]["temperature"]
    min_temp = data[0]["temperature"]

    max_date = data[0]["date"]
    min_date = data[0]["date"]

    above_zero = 0

    for day in data:
        temp = day["temperature"]

        total_temp = total_temp + temp
        count = count + 1

        if temp > max_temp:
            max_temp = temp
            max_date = day["date"]

        if temp < min_temp:
            min_temp = temp
            min_date = day["date"]

        if temp > 0:
            above_zero = above_zero + 1

    average = total_temp / count

    print("\nTemperatuuri statistika:")
    print("Keskmine temperatuur:", round(average, 2), "°C")
    print("Kõrgeim temperatuur:", max_temp, "°C (", max_date, ")")
    print("Madalaim temperatuur:", min_temp, "°C (", min_date, ")")
    print("Päevi üle 0°C:", above_zero)


def rain_stats(data: list) -> None:
    total_rain = 0

    max_rain = data[0]["rain"]
    max_date = data[0]["date"]

    no_rain_days = 0

    for day in data:
        rain = day["rain"]

        total_rain = total_rain + rain

        if rain > max_rain:
            max_rain = rain
            max_date = day["date"]

        if rain == 0:
            no_rain_days = no_rain_days + 1

    print("\nSademete analüüs:")
    print("Kogu sademete hulk:", total_rain, "mm")
    print("Kõige rohkem sadas:", max_rain, "mm (", max_date, ")")
    print("Sademeteta päevi:", no_rain_days)


def save_summary(data: list) -> None:
    total_temp = 0
    total_rain = 0
    count = 0

    max_temp = data[0]["temperature"]
    min_temp = data[0]["temperature"]

    max_date = data[0]["date"]
    min_date = data[0]["date"]

    for day in data:
        temp = day["temperature"]
        rain = day["rain"]

        total_temp = total_temp + temp
        total_rain = total_rain + rain
        count = count + 1

        if temp > max_temp:
            max_temp = temp
            max_date = day["date"]

        if temp < min_temp:
            min_temp = temp
            min_date = day["date"]

    average = total_temp / count

    with open("ilm_kokkuvote.txt", "w", encoding="utf-8") as f:
        f.write("Mõõtmiste arv: " + str(count) + "\n")
        f.write("Keskmine temperatuur: " + str(round(average, 2)) + " °C\n")
        f.write("Kogu sademete hulk: " + str(total_rain) + " mm\n")
        f.write("Kõige külmem päev: " + min_date + " (" + str(min_temp) + " °C)\n")
        f.write("Kõige soojem päev: " + max_date + " (" + str(max_temp) + " °C)\n")

    print("Kokkuvõte salvestatud faili ilm_kokkuvote.txt")


def menu():
    data = read_data("ilm.txt")

    while True:
        print("\n--- ILMAANDMED ---")
        print("1 - Kuva kõik mõõtmised")
        print("2 - Temperatuuri statistika")
        print("3 - Sademete analüüs")
        print("4 - Salvesta kokkuvõte")
        print("0 - Välju")

        choice = input("Valik: ")

        if choice == "1":
            show_all(data)
        elif choice == "2":
            temperature_stats(data)
        elif choice == "3":
            rain_stats(data)
        elif choice == "4":
            save_summary(data)
        elif choice == "0":
            print("Head aega!")
            break
        else:
            print("Vale valik!")


if __name__ == "__main__":
    menu()
