from sudoku.sudoku import Sudoku

N = 3  # Tamanho da subgrade (NxN)
sudoku = Sudoku(N)

if sudoku.solve():
    print("Solução encontrada:")
    print(sudoku)
else:
    print("Não há solução possível.")
