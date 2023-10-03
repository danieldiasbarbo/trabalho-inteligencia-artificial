class Sudoku:
    def __init__(self, N):
        self.N = N
        self.board = [[0] * (N**2) for _ in range(N**2)]

    def is_valid(self, row, col, num):
        # Verifica se o número já está na mesma linha ou coluna
        for i in range(N**2):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False

        # Verifica se o número já está na mesma subgrade NxN
        start_row, start_col = row - row % N, col - col % N
        for i in range(N):
            for j in range(N):
                if self.board[i + start_row][j + start_col] == num:
                    return False

        return True

    def solve(self):
        for row in range(N**2):
            for col in range(N**2):
                if self.board[row][col] == 0:
                    for num in range(1, N**2 + 1):
                        if self.is_valid(row, col, num):
                            self.board[row][col] = num
                            if self.solve():
                                return True
                            self.board[row][col] = 0
                    return False
        return True

    def __str__(self):
        board_str = ""
        for i in range(N**2):
            if i % N == 0 and i != 0:
                board_str += "-" * (N**2 * 2 + 3) + "\n"
            for j in range(N**2):
                if j % N == 0 and j != 0:
                    board_str += "| "
                board_str += str(self.board[i][j]) + " "
            board_str += "\n"
        return board_str


# Exemplo de uso:
N = 3  # Tamanho da subgrade (NxN)
sudoku = Sudoku(N)

if sudoku.solve():
    print("Solução encontrada:")
    print(sudoku)
else:
    print("Não há solução possível.")
