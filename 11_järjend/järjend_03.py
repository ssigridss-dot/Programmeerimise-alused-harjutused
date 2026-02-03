"""Lihtsa sõnaraamatu jaoks koosta neli järjendit (arv, eesti, inglise, itaalia) sisuga: arv - 1, 2, 3, 4
eesti - üks, kaks, kolm, neli inglise - one, two, three, four itaalia - uno, due, tre, quattro

Väljasta kõik elemendid tabelina ekraanile: 1 - üks - one - uno 2 - kaks - two - due ...

Lisa arvude ja eesti järjendile veel kaks elementi.
Kontrolli, kas itaalia sõnade järjendis eksiteerib element 'tre'
Väljasta kõigi nelja järjendi elemendid tähestikulises järjekorras kasvavalt."""

numbers = [1, 2, 3, 4]
estonian_numbers = ["üks", "kaks", "kolm", "neli"]
english_numbers = ["one", "two", "three", "four"]
italian_numbers = ["uno", "due", "tre", "quattro"]

for i in range(len(numbers)):
    print(f"{numbers[i]} - {estonian_numbers[i]:^4} - {english_numbers[i]:^5} - {italian_numbers[i]:>7}")

numbers += [5, 6]
estonian_numbers.append("viis")
estonian_numbers.append("kuus")

if "tre" in italian_numbers:
    print("'tre' eksisteerib itaalia järjendis")

print("Numbrid sorteeritud")
numbers.sort()
for number in numbers:
    print(number)

all_languages = sorted(estonian_numbers)
all_languages += sorted(english_numbers)
all_languages += sorted(italian_numbers)

print("Iga keel eraldi sorteeritud:")
for value in all_languages:
    print(value)

all_languages.sort()
print("Kõik keeled korraga sorteeritud:")
for value in all_languages:
    print(value)
