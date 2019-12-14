#opcode = [1,9,10,3,
#2,3,11,0,
#99,30,40,50]

vstup = open ('puzzle.txt', encoding='utf-8')
intcome = [x.split(',') for x in vstup][0]
opcode = [ int(x) for x in intcome]

noun = 12
verb = 2
vysledek = 100 * noun + verb
print(vysledek)
