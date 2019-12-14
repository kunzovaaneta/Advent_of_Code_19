import math
vstup = open ('1a_hodnoty.txt', encoding='utf-8')
fuel_requirements = [math.floor(int(x.strip())/3) - 2 for x in vstup]
print(sum(fuel_requirements))