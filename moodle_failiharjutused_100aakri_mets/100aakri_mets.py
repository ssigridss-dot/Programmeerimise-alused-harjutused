def calculate_growth(area_acres: float, growth_per_hectare: float) -> float:
    """
    Calculate forest`s growth per year.
    """
    hectares = area_acres * 0.4047
    growth = hectares * growth_per_hectare
    return round(growth, 2)

filename = input("Sisesta faili nimi: ")
growth_per_hectare = float(input("Sisesta aastane juurdekasv hektari kohta: "))
limit = float(input("Sisesta pindala piir aakrites: "))

count = 0
with open(filename, "r") as f:
    for line in f:
        area = float(line.strip())
        if area > limit:
            growth = calculate_growth(area, growth_per_hectare)
            print(f"Metsatüki juurdekasv on {growth} tm")
            count += 1
        else:
            print("Metsatükki ei võeta arvesse")
print(f"Arvutati {count} metsatüki juurdekasv.")