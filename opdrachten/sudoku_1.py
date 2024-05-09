from z3 import *

# Vervangen de getallen op de plekken waar 0 staat zodat aan de regels van een sudoku wordt gehouden.
# Alle rijen, kolommen, en blokken moeten 1 t/m 9 één (en dus niet meer keer) keer bevatten

# Sudoku problem
sudoku = [[Int(f'sudoku_{r}_{c}') for c in range(9)] for r in range(9)]

s = Solver()

#   Set the input
sudoku_input = [
     [0, 0, 9, 8, 5, 6, 0, 0, 0],
     [0, 8, 0, 0, 0, 9, 0, 0, 0],
     [2, 0, 0, 0, 0, 7, 0, 0, 0],
     [7, 0, 0, 0, 0, 1, 3, 9, 6],
     [9, 0, 0, 0, 6, 0, 0, 0, 5],
     [5, 3, 6, 2, 0, 0, 0, 0, 7],
     [0, 0, 0, 9, 0, 0, 0, 0, 1],
     [0, 0, 0, 3, 0, 0, 0, 6, 0],
     [0, 0, 0, 6, 8, 2, 4, 0, 0],
]

for r, row in enumerate(sudoku_input):
    for c, cell in enumerate(row):
        if cell > 0:
            s.add(sudoku[r][c] == cell)

# Define your constraints here:


if s.check() == sat:
    solution = s.model()
    for r in range(9):
        print([solution[sudoku[r][c]].as_long() if solution[sudoku[r][c]] is not None else 0 for c in range(9)])
else:
    print('no solution found')