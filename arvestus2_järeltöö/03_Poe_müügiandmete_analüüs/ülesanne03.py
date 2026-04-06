"""VARIANT 3 (LÜHIKE): POE MÜÜGIANDMETE ANALÜÜS

ÜLESANDE KIRJELDUS:
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
def read_sales(filename: str) -> list:
    sales = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(";")

            product = parts[0]
            category = parts[1]
            quantity = int(parts[2])
            price = float(parts[3])

            sale = {
                "product": product,
                "category": category,
                "quantity": quantity,
                "price": price
            }

            sales.append(sale)

    return sales


def show_all_sales(sales: list) -> None:
    total_revenue = 0

    print("\nKõik tehingud:")
    print("-" * 50)

    for sale in sales:
        revenue = sale["quantity"] * sale["price"]
        total_revenue = total_revenue + revenue

        print(sale["product"], "|", sale["quantity"], "tk |", sale["price"], "€ | summa:", round(revenue, 2), "€")

    print("\nKogutulu:", round(total_revenue, 2), "€")


def search_product(sales: list) -> None:
    query = input("Sisesta toote nimi: ").lower()

    total_quantity = 0
    total_revenue = 0
    found = False

    print("\nLeitud tehingud:")

    for sale in sales:
        product = sale["product"].lower()

        if product == query:
            revenue = sale["quantity"] * sale["price"]

            print(sale["product"], "|", sale["quantity"], "tk |", sale["price"], "€")

            total_quantity = total_quantity + sale["quantity"]
            total_revenue = total_revenue + revenue
            found = True

    if found:
        print("\nKokku müüdud kogus:", total_quantity)
        print("Kogutulu:", round(total_revenue, 2), "€")
    else:
        print("Toodet ei leitud!")


def category_analysis(sales: list) -> None:
    categories = {}

    for sale in sales:
        category = sale["category"]

        if category not in categories:
            categories[category] = {
                "count": 0,
                "revenue": 0
            }

        categories[category]["count"] = categories[category]["count"] + 1

        revenue = sale["quantity"] * sale["price"]
        categories[category]["revenue"] = categories[category]["revenue"] + revenue

    print("\nKategooriate analüüs:")
    print("-" * 50)

    max_revenue = 0
    best_category = ""

    for category in categories:
        count = categories[category]["count"]
        revenue = categories[category]["revenue"]

        print(category, "| tehinguid:", count, "| tulu:", round(revenue, 2), "€")

        if revenue > max_revenue:
            max_revenue = revenue
            best_category = category

    print("\nKõige tulutoovam kategooria:", best_category, "-", round(max_revenue, 2), "€")


def save_summary(sales: list) -> None:
    total_revenue = 0
    total_transactions = 0

    products = []

    categories = {}

    for sale in sales:
        revenue = sale["quantity"] * sale["price"]

        total_revenue = total_revenue + revenue
        total_transactions = total_transactions + 1

        # loe erinevad tooted
        if sale["product"] not in products:
            products.append(sale["product"])

        # kategooriad
        category = sale["category"]

        if category not in categories:
            categories[category] = 0

        categories[category] = categories[category] + revenue

    max_revenue = 0
    best_category = ""

    for category in categories:
        if categories[category] > max_revenue:
            max_revenue = categories[category]
            best_category = category

    with open("müük_kokkuvõte.txt", "w", encoding="utf-8") as f:
        f.write("Tehingute koguarv: " + str(total_transactions) + "\n")
        f.write("Kogu müügitulu: " + str(round(total_revenue, 2)) + " €\n")
        f.write("Erinevate toodete arv: " + str(len(products)) + "\n")
        f.write("Kõige tulutoovam kategooria: " + best_category + "\n")

    print("Kokkuvõte salvestatud faili müük_kokkuvõte.txt")


def menu():
    sales = read_sales("müük.txt")

    while True:
        print("\n--- MÜÜGIANDMED ---")
        print("1 - Kuva kõik tehingud")
        print("2 - Otsi toodet")
        print("3 - Kategooriate analüüs")
        print("4 - Salvesta kokkuvõte")
        print("0 - Välju")

        choice = input("Valik: ")

        if choice == "1":
            show_all_sales(sales)
        elif choice == "2":
            search_product(sales)
        elif choice == "3":
            category_analysis(sales)
        elif choice == "4":
            save_summary(sales)
        elif choice == "0":
            print("Head aega!")
            break
        else:
            print("Vale valik!")


if __name__ == "__main__":
    menu()