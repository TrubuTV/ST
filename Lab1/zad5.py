lista = [1, 2, 3, 11, 21, 111, 231]

for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        if str(lista[i]) > str(lista[j]):
            lista[i], lista[j] = lista[j], lista[i]

print(lista)
