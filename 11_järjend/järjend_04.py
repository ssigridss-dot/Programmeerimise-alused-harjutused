from random import randint
"""Moodusta järjend järgnevate sõnedega:

Jah, kindlasti!
Jah!
Võib-olla!
Ei!
Tee programm, kus kasutaja saab küsida jah/ei küsimuse ja programm annab vastuse ühe suvalise elemendi eelnevast järjendist.

Juhuslike arvude genereerimist vaatame tulevikus, kuid praegu lisame programmi algusesse rea, tänu millele Python suudab
 juhuslikke arve genereerida:

import random
Seejärel võime suvalises kohas programmis kasutada juhusliku arvu saamiseks funktsiooni random.randint(x, y), mis 
genereerib juhusliku täisarvu x-st y-ni (mõlemad kaasaarvatud), näiteks:

juhuarv = random.randint(1, 10)
Lisa ka sisse- ja väljajuhatavad tekstid, et dialoog kasutajaga oleks võimalikult loomulik.

Kui valmis, siis lisa järjendisse 20 erinevat vastusevarianti, mille ingliskeelsed vasted leiad leheküljelt 
https://en.wikipedia.org/wiki/Magic_8-Ball"""
answers = [
    "Jah, kindlasti!",
    "Jah!",
    "Võib-olla!",
    "Ei!"
]

def ask_magic_eight_ball():
    question = input("Palun sisesta oma Jah/ei küsimus ennustajale:")
    random_number = randint(0, len(answers) - 1)
    return answers[random_number]


if __name__ == '__main__':
    print("Tere tulemast maailmakuulsa ennustaja jutule!")
    answer = ask_magic_eight_ball()
    print(f"Ennustaja kaalus sinu küsimust põhjalikult j tuli järeldusele, et {answer}")