"""
KT 1. ülesanne 2.
1.       Küsi kasutaja nime ja vanust
2.       Kui nime pikkus on väiksem kui vanus või vanus on alla 5 siis tervita nime pidi 3 korda (Kordus)
3.       Muidu küsi kolm arvu ja nende summa
4.       Teata kas said õige tulemuse."""
def greet_or_calculate():
    name = input("Mis on sinu nimi? ")
    age = int(input("Kui vana sa oled? "))
    if len(name) < age or age < 5:
        for i in range(3):
            print(f"Tere, {name}!")
    else:
        first_number = int(input("Sisesta esimene arv: "))
        second_number = int(input("Sisesta teine arv: "))
        third_number = int(input("Sisesta kolmas arv:"))
        user_sum = int(input("Mis on nende arvude summa?"))
        right_sum = first_number + second_number + third_number
        if user_sum == right_sum:
            print("Õige vastus!")
        else:
            print(f"Vale vastus. Õige summa on {right_sum}.")

if __name__ == '__main__':
    greet_or_calculate()