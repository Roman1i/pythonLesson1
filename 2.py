def DeMorgan(x, y, z):
    f = not(x or y or z) == (not x) and (not y) and (not z)
    return f

print("X = 0; Y = 0; Z = 0; F - " + str(DeMorgan(0, 0, 0)))
print("X = 0; Y = 0; Z = 1; F - " + str(DeMorgan(0, 0, 1)))
print("X = 0; Y = 1; Z = 0; F - " + str(DeMorgan(0, 1, 0)))
print("X = 0; Y = 1; Z = 1; F - " + str(DeMorgan(0, 1, 1)))
print("X = 1; Y = 0; Z = 0; F - " + str(DeMorgan(1, 0, 0)))
print("X = 1; Y = 0; Z = 1; F - " + str(DeMorgan(1, 0, 1)))
print("X = 1; Y = 1; Z = 0; F - " + str(DeMorgan(1, 1, 0)))
print("X = 1; Y = 1; Z = 1; F - " + str(DeMorgan(1, 1, 1)))