"""ÜLESANDE KIRJELDUS:
Kauplus vajab lihtsat programmi müügiandmete analüüsimiseks.

SISENDANDMED:
Fail "müük.txt" sisaldab müügitehinguid formaaadis:
Toode;Kategooria;Kogus;Hind

Näiteks:
Piim;Piimatooted;2;1.50
Leib;Pagaritooted;1;1.20
Juust;Piimatooted;1;3.50

Kus:
- Toode (toote nimi)
- Kategooria
- Kogus (müüdud tükkides)
- Hind (ühiku hind eurodes)

ÜLESANDED:

1. Loe fail sisse ja salvesta tehingud järjendisse (iga tehing on sõnastik).

2. Kuva menüü järgmiste valikutega:
   1 - Kuva kõik tehingud
   2 - Otsi toodet
   3 - Kategooriate analüüs
   4 - Salvesta kokkuvõte
   0 - Välju

3. KUVA KÕIK TEHINGUD: Prindi välja kõik tehingud koos summa arvutusega (kogus * hind).
   Kuva ka kogutulu.

4. OTSI TOODET: Kasutaja sisestab toote nime (case-insensitive).
   - Kuva kõik selle toote tehingud
   - Arvuta kokku müüdud kogus
   - Arvuta kogutulu sellest tootest

5. KATEGOORIATE ANALÜÜS:
   - Grupeeri tehingud kategooriate kaupa
   - Iga kategooria kohta näita:
     * Tehingute arv
     * Kogutulu
   - Leia kõige tulutoovam kategooria

6. SALVESTA KOKKUVÕTE: Loo fail "müük_kokkuvõte.txt", kuhu kirjuta:
   - Tehingute koguarv
   - Kogu müügitulu
   - Erinevate toodete arv
   - Kõige tulutoovam kategooria

7. Programm peab töötama tsüklis kuni kasutaja valib "0 - Välju"
"""

def main_menu():


    while True:
        a = input("Palun vali toiming ja sisesta vastav number. \n1- soovin näha kõiki tooteid "
              "\n2- soovin otsida toodet \n3- soovin analüüsida kategoriaid "
              "\n4- soovin salvestada kokkuvõtet \n0- välju \nSoovin: ")

        if a == "1": #kuva kõik tehingud
            total_sale = 0
            with open("müük.txt", "r", encoding="utf-8") as file:
                for line in file:
                    products = line.strip().split(";")

                    quantity = int(products[2])
                    price = float(products[3])
                    total = float(quantity * price)

                    total_sale += total

                    print(f"{line.strip()}, Kokku müük: {total:.2} €")
            print(f"Kogumüük: {total_sale}")

        elif a == "2": #otsi toodet
            search = input("Sisesta toote nimi: ").lower()

            total_quantity = 0
            total_revenue = 0

            with open("müük.txt", "r", encoding="utf-8") as file:
                for line in file:
                    products = line.strip().split(";")

                    product = products[0].lower()
                    quantity = int(products[2])
                    price = float(products[3])

                    if product == search:
                        total = quantity * price

                        print(f"{line.strip()}, Kokku: {total:.2} €")

                        total_quantity += quantity
                        total_revenue += total

                        print(f"Müüdud kokku {total_quantity} tükki")
                        print(f"Toote müügitulu kokku: {total_revenue:.2} €")


        elif a == "3": #kategooriate analüüs
            categories = {}

            with open("müük.txt", "r", encoding="utf-8") as file:
                for line in file:
                    products = line.strip().split(";")

                    category = products[1]
                    quantity = int(products[2])
                    price = float(products[3])
                    total = quantity * price

                    if category not in categories:
                        categories[category] = {"count": 0, "revenue": 0}

                    categories[category]["count"] += 1
                    categories[category]["revenue"] += total

            max_category = ""
            max_revenue = 0

            for cat in categories:
                count = categories[cat]["count"]
                revenue = categories[cat]["revenue"]

                print(f"{cat}:")
                print(f"Tehingute arv: {count}")
                print(f"Kogutulu: {revenue:.2f} €")

                if revenue > max_revenue:
                    max_revenue = revenue
                    max_category = cat

            print(f"Kõige tulusam kategooria on: {max_category} müügisummaga {max_revenue:.2f}")

        elif a == "4": #salvesta kokkuvõte
            total_revenue = 0
            total_transactions = 0
            products = set()

            categories = {}

            with open("müük.txt", "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split(";")

                    product = parts[0]
                    category = parts[1]
                    quantity = int(parts[2])
                    price = float(parts[3])

                    total = quantity * price

                    total_revenue += total
                    total_transactions += 1
                    products.add(product)

                    if category not in categories:
                        categories[category] = [0, 0]

                    categories[category][0] += 1
                    categories[category][1] += total

            best_category = ""
            best_revenue = 0

            for cat in categories:
                if categories[cat][1] > best_revenue:
                    best_revenue = categories[cat][1]
                    best_category = cat

            with open("müük_kokkuvõte.txt", "w", encoding="utf-8") as file:
                file.write(f"Tehingute koguarv: {total_transactions}\n")
                file.write(f"Kogu müügitulu: {total_revenue:.2f} €\n")
                file.write(f"Erinevate toodete arv: {len(products)}\n")
                file.write(f"Kõige tulutoovam kategooria: {best_category} ({best_revenue:.2f} €)\n")

            print("Kokkuvõte salvestatud faili müük_kokkuvõte.txt")

        elif a == "0":
                print("Programm suletud!")
                break


if __name__ == '__main__':
    main_menu()