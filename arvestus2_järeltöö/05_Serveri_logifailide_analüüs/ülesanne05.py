"""VARIANT 5 (LÜHIKE): SERVERI LOGIFAILIDE ANALÜÜS

ÜLESANDE KIRJELDUS:
Veebiserver vajab lihtsat programmi logifailide analüüsimiseks.

SISENDANDMED:
Fail "server.log" sisaldab serverilogi kirjeid formaaadis:
Aeg;IP-aadress;Tüüp;Kood

Näiteks:
2024-01-15 10:23:45;192.168.1.100;INFO;200
2024-01-15 10:24:12;192.168.1.105;ERROR;500
2024-01-15 10:25:03;192.168.1.100;WARNING;404

Kus:
- Aeg (AAAA-KK-PP HH:MM:SS)
- IP-aadress
- Tüüp (INFO, WARNING, ERROR, CRITICAL)
- Kood (HTTP vastuse kood)

ÜLESANDED:

1. Loe logifail sisse ja salvesta kirjed järjendisse (iga kirje on sõnastik).

2. Kuva menüü järgmiste valikutega:
   1 - Kuva kõik logikirjed
   2 - Filtreeri tüübi järgi
   3 - IP-aadresside statistika
   4 - Salvesta raport
   0 - Välju

3. KUVA KÕIK LOGIKIRJED: Prindi välja kõik kirjed tabelina.
   Kuva ka kokkuvõte: kokku kirjeid, INFO, WARNING, ERROR, CRITICAL arv.

4. FILTREERI TÜÜBI JÄRGI: Kasutaja valib tüübi (INFO/WARNING/ERROR/CRITICAL).
   Kuva kõik selle tüübiga kirjed.
   Kuva ka protsent kõigist kirjetest.

5. IP-AADRESSIDE STATISTIKA:
   - Loe kokku iga IP-aadressi kirjete arv
   - Kuva TOP 5 aktiivsemat IP-aadressi
   - Iga IP kohta näita ka ERROR/CRITICAL kirjete arv

6. SALVESTA RAPORT: Loo fail "server_raport.txt", kuhu kirjuta:
   - Kogu kirjete arv
   - Kirjete jaotus tüüpide järgi (arv ja %)
   - TOP 3 aktiivsemat IP-aadressi
   - Süsteemi staatus (OK kui < 10% vead, muidu HOIATUS)

7. Programm peab töötama tsüklis kuni kasutaja valib "0 - Välju"
"""

def read_logs(filename: str) -> list:
    logs = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(";")

            time = parts[0]
            ip = parts[1]
            log_type = parts[2]
            code = parts[3]

            entry = {
                "time": time,
                "ip": ip,
                "type": log_type,
                "code": code
            }

            logs.append(entry)

    return logs


def show_all_logs(logs: list) -> None:
    total = 0

    info_count = 0
    warning_count = 0
    error_count = 0
    critical_count = 0

    print("\nKõik logikirjed:")
    print("-" * 70)

    for log in logs:
        print(log["time"], "|", log["ip"], "|", log["type"], "|", log["code"])

        total = total + 1

        if log["type"] == "INFO":
            info_count = info_count + 1
        elif log["type"] == "WARNING":
            warning_count = warning_count + 1
        elif log["type"] == "ERROR":
            error_count = error_count + 1
        elif log["type"] == "CRITICAL":
            critical_count = critical_count + 1

    print("\nKokku kirjeid:", total)
    print("INFO:", info_count)
    print("WARNING:", warning_count)
    print("ERROR:", error_count)
    print("CRITICAL:", critical_count)


def filter_by_type(logs: list) -> None:
    selected = input("Sisesta tüüp (INFO/WARNING/ERROR/CRITICAL): ").upper()

    total = 0
    match_count = 0

    print("\nValitud kirjed:")

    for log in logs:
        total = total + 1

        if log["type"] == selected:
            print(log["time"], "|", log["ip"], "|", log["type"], "|", log["code"])
            match_count = match_count + 1

    if total > 0:
        percent = (match_count / total) * 100
    else:
        percent = 0

    print("\nSelliseid kirjeid:", match_count)
    print("Protsent kõigist:", round(percent, 2), "%")


def ip_statistics(logs: list) -> None:
    ip_counts = {}
    ip_errors = {}

    # loe kõik
    for log in logs:
        ip = log["ip"]

        if ip not in ip_counts:
            ip_counts[ip] = 0
            ip_errors[ip] = 0

        ip_counts[ip] = ip_counts[ip] + 1

        if log["type"] == "ERROR" or log["type"] == "CRITICAL":
            ip_errors[ip] = ip_errors[ip] + 1

    print("\nIP statistika:")
    print("-" * 50)

    # leia TOP 5
    used = []

    for i in range(5):
        max_ip = ""
        max_count = -1

        for ip in ip_counts:
            if ip not in used:
                if ip_counts[ip] > max_count:
                    max_count = ip_counts[ip]
                    max_ip = ip

        if max_ip == "":
            break

        print(max_ip, "| kirjeid:", ip_counts[max_ip], "| vead:", ip_errors[max_ip])

        used.append(max_ip)


def save_report(logs: list) -> None:
    total = 0

    info = 0
    warning = 0
    error = 0
    critical = 0

    ip_counts = {}

    for log in logs:
        total = total + 1

        log_type = log["type"]

        if log_type == "INFO":
            info = info + 1
        elif log_type == "WARNING":
            warning = warning + 1
        elif log_type == "ERROR":
            error = error + 1
        elif log_type == "CRITICAL":
            critical = critical + 1

        ip = log["ip"]

        if ip not in ip_counts:
            ip_counts[ip] = 0

        ip_counts[ip] = ip_counts[ip] + 1

    # protsendid
    if total > 0:
        info_p = (info / total) * 100
        warning_p = (warning / total) * 100
        error_p = (error / total) * 100
        critical_p = (critical / total) * 100
    else:
        info_p = warning_p = error_p = critical_p = 0

    # TOP 3 IP
    used = []
    top_ips = []

    for i in range(3):
        max_ip = ""
        max_count = -1

        for ip in ip_counts:
            if ip not in used:
                if ip_counts[ip] > max_count:
                    max_count = ip_counts[ip]
                    max_ip = ip

        if max_ip == "":
            break

        top_ips.append((max_ip, max_count))
        used.append(max_ip)

    # süsteemi staatus
    error_total = error + critical

    if total > 0:
        error_percent = (error_total / total) * 100
    else:
        error_percent = 0

    if error_percent < 10:
        status = "OK"
    else:
        status = "HOIATUS"

    with open("server_raport.txt", "w", encoding="utf-8") as f:
        f.write("Kokku kirjeid: " + str(total) + "\n")

        f.write("INFO: " + str(info) + " (" + str(round(info_p, 2)) + "%)\n")
        f.write("WARNING: " + str(warning) + " (" + str(round(warning_p, 2)) + "%)\n")
        f.write("ERROR: " + str(error) + " (" + str(round(error_p, 2)) + "%)\n")
        f.write("CRITICAL: " + str(critical) + " (" + str(round(critical_p, 2)) + "%)\n")

        f.write("TOP 3 IP aadressi:\n")
        for item in top_ips:
            f.write(item[0] + " - " + str(item[1]) + "\n")

        f.write("Süsteemi staatus: " + status + "\n")

    print("Raport salvestatud faili server_raport.txt")


def menu():
    logs = read_logs("server.txt")

    while True:
        print("\n--- SERVERI LOGID ---")
        print("1 - Kuva kõik logikirjed")
        print("2 - Filtreeri tüübi järgi")
        print("3 - IP statistika")
        print("4 - Salvesta raport")
        print("0 - Välju")

        choice = input("Valik: ")

        if choice == "1":
            show_all_logs(logs)
        elif choice == "2":
            filter_by_type(logs)
        elif choice == "3":
            ip_statistics(logs)
        elif choice == "4":
            save_report(logs)
        elif choice == "0":
            print("Head aega!")
            break
        else:
            print("Vale valik!")


if __name__ == "__main__":
    menu()