from z3 import *

# Opracht 1)
# Vind een integer waarde voor x en y gegeven dat:
# x + y = 10
# x - y = 4

s = Solver()

if s.check() == sat:
    print(s.model())
else:
    print("unsat")


# Opdracht 2)
# Vind de boolean waarden van de volgende constraints:
# a∧b
# ¬c
# c ⇒ a

s = Solver()

if s.check() == sat:
    print(s.model())
else:
    print("unsat")