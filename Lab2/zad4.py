def hanoi(n, A, B, C):
    if n == 1:
        print("Przenieś krążek z", A, "na", C)
    else:
        hanoi(n-1, A, C, B)
        print("Przenieś krążek z", A, "na", C)
        hanoi(n-1, B, A, C)


hanoi(5, 'A', 'B', 'C')
