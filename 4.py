n = int(input('Номер четверти: '))

while not(0 < n < 5):
    n = int(input('Номер четверти: '))

if n == 1:
    print('X ∈ (0, +∞); Y ∈ (0, +∞)')
elif n == 2:
    print('X ∈ (-∞, 0); Y ∈ (0, +∞)')
elif n == 3:
    print('X ∈ (-∞, 0); Y ∈ (-∞, 0)')
elif n == 4:
    print('X ∈ (0, +∞); Y ∈ (-∞, 0)')


