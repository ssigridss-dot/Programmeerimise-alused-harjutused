"""
Kt 1.

1.       Küsi kasutajalt 3 arvu
2.       Väikseim arv korruta kahega
3.       Küsi kasutajalt arvude ruute ühest kuni eelmise sammu tulemuseni (Kordus)
4.       Teata kas kasutaja vastas õigesti või valesti
5.       Teata mitu korda kasutaja vastas õigesti."""

def main():
    a = int(input("Sisesta esimene arv: "))
    b = int(input("Sisesta teine arv: "))
    c = int(input("Sisesta kolmas arv: "))
    min_number = min(a,b,c)
    last_value = min_number * 2
    print(f"Väikseim arv on {min_number}, korrutatuna kahega = {last_value}.")


    right_answers = 0
    for i in range(1, last_value + 1):
        answer = int(input(f"Mis on arvu {i} ruut? "))
        if answer == i ** 2:
            print("Õige!")
            right_answers += 1
        else:
            print(f"Vale! Õige vastus on {i**2}.")
    print(f"Sa vastasid õigesti {right_answers} korda.")


if __name__ == '__main__':
    main()
