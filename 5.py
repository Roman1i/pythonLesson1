import math

ax = int(input('Координата x первой точки: '))
ay = int(input('Координата y первой точки: '))
bx = int(input('Координата x второй точки: '))
by = int(input('Координата y второй точки: '))

print(round(math.sqrt((bx - ax)**2 + (by - ay)**2), 2))
