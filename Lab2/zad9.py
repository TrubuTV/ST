dzialania = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}

stos = []
wyrazenie = '7+2*(3*4+6/3)'
onp = ''

for w in wyrazenie:
    if w == '(':
        stos.append(w)
    elif w == ')':
        w_stos = stos.pop()
        while w_stos != '(':
            onp += w_stos
            w_stos = stos.pop()
    elif w in dzialania.keys():
        while len(stos) > 0 and stos[-1] != '(' and dzialania[stos[-1]] >= dzialania[w]:
            onp += stos.pop()
        stos.append(w)
    else:
        onp += w
else:
    while len(stos) > 0:
        onp += stos.pop()

print(onp)
