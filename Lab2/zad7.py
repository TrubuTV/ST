def dziel_i_zwyciezaj(n, start, end):
    if start == end:
        return n[start]  # pojedynczy element

    mid = (start + end) // 2

    # rekurencyjne wywołanie dla lewej połowy
    left_sum = dziel_i_zwyciezaj(n, start, mid)
    # rekurencyjne wywołanie dla prawej połowy
    right_sum = dziel_i_zwyciezaj(n, mid + 1, end)

    return left_sum + right_sum  # suma lewej i prawej połowy


n = [2, 4, 6, 8, 10]
len = len(n)
wynik = dziel_i_zwyciezaj(n, 0, len-1)
print("Suma elementów w tablicy:", wynik)
