n = int(input("Podaj ilość liczb w ciągu: "))
ile_u = 0

if n > 0:
    ile_u = 0
    i = 0
    for i in range(n):
        ai = int(input(f"Podaj {i+1}. liczbę: "))
        if ai < 0:
            ile_u += 1
else:
    print(f"Podaj jeszcze raz n")
print(f"Ilość liczb ujemnych: {ile_u}")
