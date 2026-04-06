"""VARIANT 1 (LÜHIKE): RAAMATUKOGU HALDUSSÜSTEEM

ÜLESANDE KIRJELDUS:
Raamatukogu vajab lihtsustatud programmi raamatute ja laenutuste haldamiseks.

SISENDANDMED:
Fail "raamatud.txt" sisaldab raamatute andmeid formaaadis:
ID;Pealkiri;Autor;Aasta

Näiteks:
1;Tõde ja õigus;A. H. Tammsaare;1926
2;Kevade;Oskar Luts;1912
3;Python algajale;John Smith;2020

Fail "laenud.txt" sisaldab laenutuste andmeid formaaadis:
RaamatuID;LaenutatuNimi

Näiteks:
1;Mati Maasikas
3;Kati Kask
1;Peeter Puu

ÜLESANDED:

1. Loe mõlemad failid sisse ja salvesta andmed (raamatud sõnastikku, laenud järjendisse).

2. Kuva menüü järgmiste valikutega:
   1 - Kuva kõik raamatud
   2 - Otsi raamatut (autor või pealkiri)
   3 - Laenutusstatistika
   4 - Salvesta raport
   0 - Välju

3. KUVA KÕIK RAAMATUD: Prindi välja kõik raamatud (ID, pealkiri, autor, aasta).

4. OTSI RAAMATUT: Kasutaja sisestab otsingutermin.
   Otsi pealkirjast ja autorist (case-insensitive).
   Kui ei leitud, teata sellest.

5. LAENUTUSSTATISTIKA:
   - Arvuta iga raamatu laenutuste arv
   - Kuva raamatud koos laenutuste arvuga
   - Leia ja kuva kõige populaarsem raamat

6. SALVESTA RAPORT: Loo fail "raport.txt", kuhu kirjuta:
   - Raamatute koguarv
   - Laenutuste koguarv
   - Kõige populaarsem raamat (koos laenutuste arvuga)
   - Raamatud, mida pole üldse laenutatud

7. Programm peab töötama tsüklis kuni kasutaja valib "0 - Välju"
"""
def read_books(filename: str) -> dict:
    books = {}

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(";")

            book_id = parts[0]
            title = parts[1]
            author = parts[2]
            year = parts[3]

            books[book_id] = {
                "title": title,
                "author": author,
                "year": year
            }

    return books


def read_loans(filename: str) -> list:
    loans = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(";")

            book_id = parts[0]
            person = parts[1]

            loan = {
                "book_id": book_id,
                "person": person
            }

            loans.append(loan)

    return loans


def show_books(books: dict) -> None:
    print("\nKõik raamatud:")
    print("-" * 50)

    for book_id in books:
        book = books[book_id]
        print(book_id, "|", book["title"], "|", book["author"], "|", book["year"])


def search_books(books: dict) -> None:
    query = input("Sisesta otsingusõna: ").lower()

    found = False

    for book_id in books:
        book = books[book_id]

        title = book["title"].lower()
        author = book["author"].lower()

        if query in title or query in author:
            print(book_id, "|", book["title"], "|", book["author"], "|", book["year"])
            found = True

    if found is False:
        print("Raamatut ei leitud!")


def loan_stats(books: dict, loans: list) -> None:
    counts = {}

    # algväärtusta kõik raamatud 0-ga
    for book_id in books:
        counts[book_id] = 0

    # loe laenutused kokku
    for loan in loans:
        book_id = loan["book_id"]
        counts[book_id] = counts[book_id] + 1

    print("\nLaenutusstatistika:")
    print("-" * 50)

    max_count = 0
    max_book_id = ""

    for book_id in counts:
        count = counts[book_id]
        book = books[book_id]

        print(book["title"], "-", count, "laenutust")

        if count > max_count:
            max_count = count
            max_book_id = book_id

    print("\nKõige populaarsem raamat:")
    print(books[max_book_id]["title"], "-", max_count, "laenutust")


def save_report(books: dict, loans: list) -> None:
    counts = {}

    for book_id in books:
        counts[book_id] = 0

    for loan in loans:
        book_id = loan["book_id"]
        counts[book_id] = counts[book_id] + 1

    total_books = 0
    for _ in books:
        total_books = total_books + 1

    total_loans = 0
    for _ in loans:
        total_loans = total_loans + 1

    max_count = 0
    max_book_id = ""

    for book_id in counts:
        if counts[book_id] > max_count:
            max_count = counts[book_id]
            max_book_id = book_id

    with open("raport.txt", "w", encoding="utf-8") as f:
        f.write("Raamatute koguarv: " + str(total_books) + "\n")
        f.write("Laenutuste koguarv: " + str(total_loans) + "\n")

        f.write("Kõige populaarsem raamat: ")
        f.write(books[max_book_id]["title"] + " (" + str(max_count) + " laenutust)\n")

        f.write("Laenutamata raamatud:\n")

        for book_id in counts:
            if counts[book_id] == 0:
                f.write(books[book_id]["title"] + "\n")

    print("Raport salvestatud faili raport.txt")


def menu():
    books = read_books("raamatud.txt")
    loans = read_loans("laenud.txt")

    while True:
        print("\n--- RAAMATUKOGU ---")
        print("1 - Kuva kõik raamatud")
        print("2 - Otsi raamatut")
        print("3 - Laenutusstatistika")
        print("4 - Salvesta raport")
        print("0 - Välju")

        choice = input("Valik: ")

        if choice == "1":
            show_books(books)
        elif choice == "2":
            search_books(books)
        elif choice == "3":
            loan_stats(books, loans)
        elif choice == "4":
            save_report(books, loans)
        elif choice == "0":
            print("Head aega!")
            break
        else:
            print("Vale valik!")


if __name__ == "__main__":
    menu()