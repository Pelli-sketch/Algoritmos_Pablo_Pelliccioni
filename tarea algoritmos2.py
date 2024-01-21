anno = int(input("Ingresa un anno entre 1900 y 2199: "))

print("Es bisiesto" if not anno % 4 and (anno % 100 or  not anno % 400) else "No es bisiesto")

# incia un counter para los años biciestos
annos_biciestos = 0

# Iterate through each year between 1900 and the given year
for anno in range(1900, anno + 1):
    # verifico si el año es biciesto
    if anno % 4 == 0 and (anno % 100 != 0 or anno % 400 == 0):
        annos_biciestos += 1 # si el año es biciesto, incrementa el counter

print("Cantidad de años biciestos entre 1900 y", anno, "es:", annos_biciestos)
