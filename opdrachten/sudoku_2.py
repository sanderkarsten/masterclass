from z3 import *

# Vervangen de getallen op de plekken waar 0 staat zodat aan de regels van een sudoku wordt gehouden.
# Alle rijen, kolommen, en blokken moeten 1 t/m 9 één (en dus niet meer keer) keer bevatten.
# Het symbool 'O' betekent dat de twee getallen aan beide zijden opeenvolgend moeten zijn (precies 1 van elkaar verschillen).
# Het symbool '<' betekent dat het getal aan de linkerzijde kleiner moet zijn dan het getal aan de rechterzijde.
# Voor het gemak zijn alle posities met een 'O' op een verticale of horizontale al gedefinieerd.

# Sudoku problem
sudoku = [[Int(f'sudoku_{r}_{c}') for c in range(9)] for r in range(9)]

s = Solver()

#   Set the input
sudoku_input = [[0 for i in range(9)] for _ in range(9)]
horizontal_o = [((0, 1), (0, 2)), ((0, 3), (0, 4)), ((0, 6), (0, 7)), ((2, 1), (2, 2)), ((2, 3), (2, 4)), ((2, 4), (2, 5)), ((4, 0), (4, 1)), ((4, 1), (4, 2)), ((4, 3), (4, 4)), ((4, 5), (4, 6)), ((4, 7), (4, 8)), ((5, 2), (5, 3)), ((6, 2), (6, 3)), ((7, 5), (7, 6))]
vertical_o = [((0, 5), (1, 5)), ((1, 6), (2, 6)), ((2, 6), (3, 6)), ((2, 8), (3, 8)), ((3, 2), (4, 2)), ((3, 6), (4, 6)), ((3, 8), (4, 8)), ((5, 2), (6, 2)), ((5, 3), (6, 3)), ((5, 5), (6, 5)), ((5, 6), (6, 6))]
os = horizontal_o + vertical_o


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