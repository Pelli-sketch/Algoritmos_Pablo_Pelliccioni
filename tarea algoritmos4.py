def es_bisiesto(año):
	return not año % 4 and (año % 100 or not año % 400)
    