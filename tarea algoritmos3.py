año = 1980

print("Es bisiesto" if not año % 4 and (año % 100 or  not año % 400) else "No es bisiesto")