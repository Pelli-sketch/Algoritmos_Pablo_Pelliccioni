from calendar import isleap

for anno in range(1980, 2199):
	if isleap(anno):
		print(anno, end=' ')