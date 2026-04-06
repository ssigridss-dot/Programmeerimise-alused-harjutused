"""VARIANT 4 (LÜHIKE): ÕPILASTE TULEMUSTE ANALÜÜS

ÜLESANDE KIRJELDUS:
Kool vajab lihtsat programmi õpilaste hinnete analüüsimiseks.

SISENDANDMED:
Fail "õpilased.txt" sisaldab õpilaste andmeid formaaadis:
Nimi;Klass

Näiteks:
Mati Maasikas;10A
Kati Kask;10B
Peeter Puu;10A

Fail "hinded.txt" sisaldab hindeid formaaadis:
Nimi;Aine;Hinne

Näiteks:
Mati Maasikas;Matemaatika;4
Mati Maasikas;Eesti keel;5
Kati Kask;Matemaatika;5

ÜLESANDED:

1. Loe mõlemad failid sisse ja salvesta andmed.

2. Kuva menüü järgmiste valikutega:
   1 - Kuva kõik õpilased
   2 - Õpilase hinded
   3 - Klassi statistika
   4 - Salvesta kokkuvõte
   0 - Välju

3. KUVA KÕIK ÕPILASED: Prindi välja kõik õpilased koos klassiga.

4. ÕPILASE HINDED: Kasutaja sisestab õpilase nime.
   - Kuva õpilase klass
   - Kuva kõik tema hinded
   - Arvuta keskmine hinne
   - Määra, kas õpilane läbis (kõik hinded >= 3)

5. KLASSI STATISTIKA: Kasutaja sisestab klassi (nt "10A").
   - Kuva klassis olevad õpilased
   - Arvuta klassi keskmine hinne
   - Leia klassi parim õpilane (kõrgeim keskmine)

6. SALVESTA KOKKUVÕTE: Loo fail "tulemused_kokkuvõte.txt", kuhu kirjuta:
   - Õpilaste arv
   - Hinnete arv
   - Üldine keskmine hinne
   - Parim õpilane (kõrgeim keskmine)

7. Programm peab töötama tsüklis kuni kasutaja valib "0 - Välju"""

def read_students(filename: str) -> dict:
    students = {}

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(";")

            name = parts[0]
            class_name = parts[1]

            students[name] = class_name

    return students


def read_grades(filename: str) -> list:
    grades = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(";")

            name = parts[0]
            subject = parts[1]
            grade = int(parts[2])

            entry = {
                "name": name,
                "subject": subject,
                "grade": grade
            }

            grades.append(entry)

    return grades


def show_students(students: dict) -> None:
    print("\nÕpilased:")
    print("-" * 40)

    for name in students:
        print(name, "| klass:", students[name])


def student_grades(students: dict, grades: list) -> None:
    name = input("Sisesta õpilase nimi: ")

    if name not in students:
        print("Õpilast ei leitud!")
        return

    print("\nÕpilane:", name)
    print("Klass:", students[name])

    total = 0
    count = 0
    passed = True

    print("Hinded:")

    for entry in grades:
        if entry["name"] == name:
            print(entry["subject"], ":", entry["grade"])

            total = total + entry["grade"]
            count = count + 1

            if entry["grade"] < 3:
                passed = False

    if count > 0:
        average = total / count
        print("Keskmine hinne:", round(average, 2))
    else:
        print("Hindeid ei leitud!")
        return

    if passed:
        print("Õpilane on läbinud")
    else:
        print("Õpilane ei läbinud")


def class_stats(students: dict, grades: list) -> None:
    class_name = input("Sisesta klass: ")

    class_students = []

    for name in students:
        if students[name] == class_name:
            class_students.append(name)

    if len(class_students) == 0:
        print("Klassi ei leitud!")
        return

    print("\nKlassi õpilased:")
    for name in class_students:
        print(name)

    total = 0
    count = 0

    best_average = 0
    best_student = ""

    for name in class_students:
        student_total = 0
        student_count = 0

        for entry in grades:
            if entry["name"] == name:
                student_total = student_total + entry["grade"]
                student_count = student_count + 1

        if student_count > 0:
            avg = student_total / student_count

            total = total + student_total
            count = count + student_count

            if avg > best_average:
                best_average = avg
                best_student = name

    if count > 0:
        class_average = total / count
        print("\nKlassi keskmine hinne:", round(class_average, 2))

    print("Parim õpilane:", best_student, "(", round(best_average, 2), ")")


def save_summary(students: dict, grades: list) -> None:
    student_count = 0
    for _ in students:
        student_count = student_count + 1

    grade_count = 0
    total = 0

    for entry in grades:
        total = total + entry["grade"]
        grade_count = grade_count + 1

    if grade_count > 0:
        overall_avg = total / grade_count
    else:
        overall_avg = 0

    best_average = 0
    best_student = ""

    for name in students:
        student_total = 0
        student_count_inner = 0

        for entry in grades:
            if entry["name"] == name:
                student_total = student_total + entry["grade"]
                student_count_inner = student_count_inner + 1

        if student_count_inner > 0:
            avg = student_total / student_count_inner

            if avg > best_average:
                best_average = avg
                best_student = name

    with open("tulemused_kokkuvõte.txt", "w", encoding="utf-8") as f:
        f.write("Õpilaste arv: " + str(student_count) + "\n")
        f.write("Hinnete arv: " + str(grade_count) + "\n")
        f.write("Üldine keskmine hinne: " + str(round(overall_avg, 2)) + "\n")
        f.write("Parim õpilane: " + best_student + " (" + str(round(best_average, 2)) + ")\n")

    print("Kokkuvõte salvestatud faili tulemused_kokkuvõte.txt")


def menu():
    students = read_students("õpilased.txt")
    grades = read_grades("hinded.txt")

    while True:
        print("\n--- ÕPILASTE TULEMUSED ---")
        print("1 - Kuva kõik õpilased")
        print("2 - Õpilase hinded")
        print("3 - Klassi statistika")
        print("4 - Salvesta kokkuvõte")
        print("0 - Välju")

        choice = input("Valik: ")

        if choice == "1":
            show_students(students)
        elif choice == "2":
            student_grades(students, grades)
        elif choice == "3":
            class_stats(students, grades)
        elif choice == "4":
            save_summary(students, grades)
        elif choice == "0":
            print("Head aega!")
            break
        else:
            print("Vale valik!")


if __name__ == "__main__":
    menu()