vstup = open ('puzzle.txt', encoding='utf-8')
intcome = [x.split(',') for x in vstup][0]
intcome = [ int(x) for x in intcome]

def int_computer (intcome):
	for i, x in enumerate(intcome):
		if i % 4 == 0:
			promenna = intcome[i]
			if promenna == 1:
				pozice_prvni = intcome[i+1]
				pozice_druha = intcome[i+2] 
				result = intcome[pozice_prvni] + intcome[pozice_druha]
				pozice_result = intcome[i+3]
				intcome[pozice_result] = result
			elif promenna == 2:
				pozice_prvni = intcome[i + 1] 
				pozice_druha = intcome[i + 2] 
				result = intcome[pozice_prvni] * intcome[pozice_druha]
				pozice_result = intcome[i + 3]
				intcome[pozice_result] = result
			elif promenna == 99:
				break
	return intcome
	
print(int_computer(intcome))