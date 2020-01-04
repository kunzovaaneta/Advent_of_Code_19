input_range = [134564,585159]
#input_range = [111111,111121]

def password(input_):
	pocet_hesel = 0
	for cislo in range(input_[0],input_[1]+1):
		seznam_c = [int(c) for c in str(cislo)]
		dvojce = any([seznam_c[i] == seznam_c[i+1] for i in range(len(seznam_c)-1)])
		#print(dvojce)
		stoupajici = any([seznam_c[i] > seznam_c[i+1] for i in range(len(seznam_c)-1)])
		#print(stoupajici)
		if dvojce and not stoupajici:
			pocet_hesel += 1
	return pocet_hesel

print(password(input_range))