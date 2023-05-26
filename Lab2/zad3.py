dec = int(input("Podaj liczbę dziesiętną: "))

binary = ""

while dec > 0:
    r = dec % 2
    binary = str(r) + binary
    dec //= 2

print("Liczba binarna: ", binary)
