from z3 import *

# Opracht 3)
# Genereer 5 getallen waar alle getallen:
# >1 en < 10 zijn
# uniek (Distinct) zijn
getallen = [Int(f'x_{i}') for i in range(5)]

s = Solver()

if s.check() == sat:
    print(s.model())
else:
    print("unsat")


# Opdracht 4)
# Genereer 10 getallen waar alle getallen:
# <100 zijn
# deelbaar zijn door hun index
# waar de som van de getallen maximaal is

o = Optimize()

if o.check() == sat:
    print(o.model())
else:
    print("unsat")