def es_bisiesto(anno):
	return not anno % 4 and (anno % 100 or not anno % 400)


for anno in range(1900, 2199):
	if es_bisiesto(anno):
		print(anno, end=' ')