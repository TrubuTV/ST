def NWDRek(a, b):
    if a != b:
        if a > b:
            return NWDRek(a-b, b)
        else:
            return NWDRek(a, b-a)
    return a

# II wersja


def nwd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def nwdRek(a, b):
    if b != 0:
        return nwdRek(b, a % b)
    return a
