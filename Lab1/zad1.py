import math

a = float(input("Podaj wartość a: "))
b = float(input("Podaj wartość b: "))
c = float(input("Podaj wartość c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("Brak pierwiastków rzeczywistych")
elif delta == 0:
    x = -b / (2*a)
    print("Jeden pierwiastek rzeczywisty: x =", x)
else:
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print("Dwa pierwiastki rzeczywiste: x1 =", x1, ", x2 =", x2)
