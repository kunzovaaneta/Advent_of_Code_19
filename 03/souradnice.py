#pohyby_A = ['R8','U5','L5','D3']
#pohyby_B = ['U7','R6','D4','L4']

with open('pohyby_A.txt', encoding='utf-8') as a:
	pohyby_A = [x.strip().split(',') for x in a][0]
with open('pohyby_B.txt', encoding='utf-8') as b:
	pohyby_B = [x.strip().split(',') for x in b][0]


def seznam_pohybu(A):
	posun_x = {
		'U' : 0, 
		'D' : 0,
		'R' : 1,
		'L' : -1
		}

	posun_y = {
		'U' : 1, 
		'D' : -1,
		'R' : 0,
		'L' : 0
		}

	x = 0
	y = 0
	delka = 0
	seznam_pohybu = dict()

	for a in A:
		smer = a[0]
		assert smer in ['U','D','R','L'] # kontrola
		posun = int(a[1:])
		for _ in range(posun):
			x += posun_x[smer]
			y += posun_y[smer]
			delka += 1
			seznam_pohybu[(x,y)] = delka
	return seznam_pohybu
	
seznam_pohybu_A = seznam_pohybu(pohyby_A)
seznam_pohybu_B = seznam_pohybu(pohyby_B)

prunik = set(seznam_pohybu_A.keys())&set(seznam_pohybu_B.keys())
#print(set(seznam_pohybu_A.keys()))
#print(prunik)

min_vzdalenost = min([abs(x) + abs(y) for (x,y) in prunik])
print('Výsledek první části je {}.'.format(min_vzdalenost))

min_delka_pruniku = min([seznam_pohybu_A[x] + seznam_pohybu_B[x] for x in prunik])
print('Výsledek druhé části je {}.'.format(min_delka_pruniku))