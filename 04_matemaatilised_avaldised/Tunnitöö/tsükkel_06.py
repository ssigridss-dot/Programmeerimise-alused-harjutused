"""Väljasta ekraanile kõikvõimalikud kombinatsioonid kujul "x - y - z", kus x, y ja z on mistahes
täisarvud 1-st 20-ni (20 kaasaarvatud). Samuti loenda, mitu sellist kombinatsiooni leiti. """
count = 0
for z in range(20):
    for y in range(20):
        for x in range(20):
            print(f" - {x + 1} - {y + 1} - {z + 1}")
            count += 1
print(f"Kokku leiti {count} kombinatsiooni.")
