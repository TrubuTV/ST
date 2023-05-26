def rek_dynamicznie(n):
    if n == 0 or n == 1:
        return 1

    tab = [None] * (n + 1)
    tab[0] = 1
    tab[1] = 1

    for i in range(2, n + 1):
        tab[i] = 2 * tab[i-1] - tab[i-2]

    return tab[n]


n = int(input("Podaj n: "))
if n >= 0:
    result = rek_dynamicznie(n)
    print("Wyraz nr", n, "ciągu to", result)
else:
    print("Nieprawidłowe dane")
