from z3 import *

# 2*vierkant + cirkel = 16
# 3* driehoek = 27
# vierkant * driehoek = 6
# vierkant * cirkel * driehoek = ?

vierkant = Real('vierkant')
driehoek = Real('driehoek')
cirkel = Real('cirkel')
answer = Int('answer')

s = Solver()

s.add((2 * vierkant) + cirkel == 16)
s.add(3 * driehoek == 27)
s.add(vierkant * driehoek == 6)
s.add(vierkant * cirkel * driehoek == answer)

print(s.check())
print(s.model())