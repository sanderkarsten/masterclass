from z3 import *

x = Int('x')
y = Int('y')
z = Int('z')

s = Solver()

s.add(3*x + 2*y - z == 1)
s.add(2*x - 2*y + 4*z == -2)
s.add(x + y + z == 222)


if s.check() == sat:
    print(s.model())
else:
    print("unsat :(")