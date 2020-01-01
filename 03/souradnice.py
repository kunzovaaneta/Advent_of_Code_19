pohyby = ('R8','U5','L5','D3')

souradnice = [0,0]
#R/L = right/left - plus/minus one on first position
#U/D = up/down - plus/minus one on second position

for pohyb in pohyby:
	if pohyb[0] == 'R':
		souradnice[0] = souradnice[0] + int(pohyb[1:])
	#	print(souradnice)
	elif pohyb[0] == 'L':
		souradnice[0] = souradnice[0] - int(pohyb[1:])
	elif pohyb[0] == 'U':
		souradnice[1] = souradnice[1] + int(pohyb[1:])
	#	print(souradnice)
	elif pohyb[0] == 'D':
		souradnice[1] = souradnice[1] - int(pohyb[1:])
print(souradnice)