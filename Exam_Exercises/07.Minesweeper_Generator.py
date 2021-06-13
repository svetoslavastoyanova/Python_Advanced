def check_for_bombs(matrix, row, col):
    bomb_counts = 0
    if 0 <= row < len(matrix) and 0 <= col+1 < len(matrix) and matrix[row][col+1] == "*":
        bomb_counts += 1
    if 0 <= row < len(matrix) and 0 <= col-1 < len(matrix) and matrix[row][col-1] == "*":
        bomb_counts += 1
    if 0 <= row-1 < len(matrix) and 0 <= col < len(matrix) and matrix[row-1][col] == "*":
        bomb_counts += 1
    if 0 <= row+1 < len(matrix) and 0 <= col < len(matrix) and matrix[row+1][col] == "*":
        bomb_counts += 1
    if 0 <= row+1 < len(matrix) and 0 <= col+1 < len(matrix) and matrix[row+1][col+1] == "*":
        bomb_counts += 1
    if 0 <= row + 1 < len(matrix) and 0 <= col-1 < len(matrix) and matrix[row+1][col-1] == "*":
        bomb_counts += 1
    if 0 <= row - 1 < len(matrix) and 0 <= col+1 < len(matrix) and matrix[row-1][col+1] == "*":
        bomb_counts += 1
    if 0 <= row - 1 < len(matrix) and 0 <= col-1 < len(matrix) and matrix[row-1][col-1] == "*":
        bomb_counts += 1
    matrix[row][col] = str(bomb_counts)
    return matrix[row][col]


rows = int(input())
cols = rows
bombs = int(input())
matrix = [["0" for j in range(cols)]for i in range(rows)]


for _ in range(bombs):
    position = input()
    position_row = int(position[1])
    position_col = int(position[4])
    matrix[position_row][position_col] = "*"

for row in range(rows):
    for col in range(cols):
        if matrix[row][col] != "*":
            check_for_bombs(matrix, row, col)

for row in matrix:
    print(' '.join(row))
