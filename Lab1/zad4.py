n = int(input("Podaj długość tablicy: "))
tablica = []

for i in range(n):
    element = int(input("Podaj element: "))
    tablica.append(element)

min_wartosc = tablica[0]

for i in range(1, n):
    if tablica[i] < min_wartosc:
        min_wartosc = tablica[i]

print("Minimalna wartość w tablicy to:", min_wartosc)
