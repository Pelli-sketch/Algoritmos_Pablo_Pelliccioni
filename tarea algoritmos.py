anno = 1980 #el año que queremos comprobar

if anno % 4 != 0: #no divisible entre 4
	print("No es bisiesto")
elif anno % 4 == 0 and anno % 100 != 0: #divisible entre 4 y no entre 100 o 400
	print("Es bisiesto")
elif anno % 4 == 0 and anno % 100 == 0 and anno % 400 != 0: #divisible entre 4 y 10 y no entre 400
	print("No es bisiesto")
elif anno % 4 == 0 and anno % 100 == 0 and anno % 400 == 0: #divisible entre 4, 100 y 400
	print("Es bisiesto")