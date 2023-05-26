def dwumian(n, m):
    if m < 0 or m > n:
        return 0
    if m == 0 or m == n:
        return 1

    tab = [[0] * (m+1) for i in range(n+1)]

    for i in range(n+1):
        tab[i][0] = 1
        if i <= m:
            tab[i][i] = 1

    for i in range(1, n+1):
        for j in range(1, min(i, m)+1):
            tab[i][j] = tab[i-1][j-1] + tab[i-1][j]

    return tab[n][m]


n = 10
m = 3
result = dwumian(n, m)
print(f"Współczynnik dwumianowy ({n} nad {m}) = {result}")
