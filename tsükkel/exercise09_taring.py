from random import randint
"""Koosta programm, mis "viskab täringut" kolm korda ehk väljastab ekraanile 3 juhusliku 
täringuviske tulemused. Et ekraanipilt oleks realistlikum, esita tulemused graafiliselt, 
selleks kasuta nn. ASCII graafikat (https://en.wikipedia.org/wiki/ASCII_art): imiteeri tekstisümbolite 
abil täringu külje kujutist. Täiendamiseks:

Kasutaja võib alguses ise valida, mitu korda täringut visata.
Mängida võib mitu inimest, programmi alguses küsitakse inimeste nimesid.
Täringut imiteeritakse kolmemõõtmelisena."""
def throw_dice() -> tuple[int, str]:
    throw_result = randint(1,6)
    return throw_result, dice_ascii[throw_result-1]


if __name__ == '__main__':
    throw_count = input("Sisesta täringuvisete arv: ")
    if throw_count.isdigit():
        throw_count = int(throw_count)
    else:
        throw_count = 3
    players_count = input("Mitu mängijat? ")
    if not players_count.isdigit():
        for i in range(throw_count)
