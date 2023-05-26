def znajdz_wektor(vektor):
    length = len(vektor)

    # Warunek zakończenia - gdy wektor jest pusty
    if length == 0:
        return None

    najw_element = vektor[0]

    for i in range(1, length):
        element = vektor[i]
        if element > najw_element:
            najw_element = element

    return najw_element


# Przykładowe użycie algorytmu
vektor = [3, 7, 2, 9, 4, 1, 6, 8, 5]
najw_element = znajdz_wektor(vektor)
print("Największy element wektora:", najw_element)
