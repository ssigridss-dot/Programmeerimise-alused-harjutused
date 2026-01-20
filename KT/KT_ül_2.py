"""Kt 2.

1.       Küsi kasutaja nime ja vanust
2.       Kui nime pikkus on väiksem kui vanus või vanus on alla 5 siis tervita nime pidi 3 korda (Kordus)
3.       Muidu küsi kolm arvu ja nende summa
4.       Teata kas said õige tulemuse."""

def greeting():
    name = input("Mis on sinu nimi?: ")
    age = int(input("Kui vana sa oled?: "))
    if age < 5:
        return f"Tere {name}!" * 3


def right_answer():
    first_number = int(input("Sisesta esimene arv: "))
    second_number = int(input("Sisesta teine arv: "))
    third_number = int(input("Sisesta kolmas arv: "))
    calculate_numbers = int(input("Mis on nende sisestatud arvude summa? "))
    right_answer = first_number + second_number + third_number
    if calculate_numbers != right_answer:
        print(f"Õige vastus on {right_answer}.")
    else:
        print(f"Tubli! Said õige vastuse.")


if __name__ == '__main__':
    greeting()
    right_answer()
