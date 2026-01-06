"""Koosta programm, mis küsib kasutajalt arvu N ja väljastab O-tähtedest koosneva ruudu suuruses NxN. Seejärel muutke
programmi nii, et ruudu diagonaalidel olevad märgid oleksid X-d"""

def draw_square(size: int, symbol: str, alt: str):

    for row in range(size):
        for col in range (size):
            #print (f"{symbol}", end=" ")
            if row == col or row + col == size - 1:
                print(f"{alt}", end=" ")
            else:
                print(f"{'o'}", end=" ")


if __name__ == '__main__':
    size = int(input("Kui suurt ruutu soovid? "))
    draw_square(size, "o", "x")
    draw_square(size * 2, "I", "-")