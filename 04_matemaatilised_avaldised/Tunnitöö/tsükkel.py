"""Koosta programm, mis küsib kasutajalt nime ja tervitab teda nimeliselt 5 korda ja lisab ka tervituse
järjekorranumber."""



if __name__ == '__main__':
    name = input("Sisesta oma nimi: ")
    for i in range(5):
        print(f"{i+1}. Tere {name}!")