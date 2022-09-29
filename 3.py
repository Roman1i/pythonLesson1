x = int(input('X: '))
while x == 0:
    x = int(input('X: '))
y = int(input('Y: '))
while y == 0:
    y = int(input('Y: '))
if x > 0:
    if y > 0:
        print('1')
    else:
        print('4')
elif x < 0:
    if y > 0:
        print('2')
    else:
        print('3')

