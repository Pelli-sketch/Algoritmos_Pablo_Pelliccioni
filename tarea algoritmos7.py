anno1 = int(input("Tell me one date: "))
anno2 = int(input("Tell me another date: "))

counter = 0  # Inicias el contador a 0
if anno1 < anno2:
    print ("Leap years between", anno1, "and", anno2, "are: ")
while anno1 <= anno2:
    if anno1 % 4 == 0 and anno1 % 100 != 0 or anno1 % 400 == 0:
        counter += 1
    anno1 += 1

print(counter)