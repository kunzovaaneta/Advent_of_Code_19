import math

vstup = open ('1a_hodnoty.txt', encoding='utf-8')
mass = [int(x.strip()) for x in vstup]

seznam_spotreby= []

for spotreba in mass:
	while spotreba >= 0:
		spotreba = math.floor(spotreba/3) -2
		if spotreba < 0:
			break
		else:
			seznam_spotreby.append(spotreba)

print(sum(seznam_spotreby))
