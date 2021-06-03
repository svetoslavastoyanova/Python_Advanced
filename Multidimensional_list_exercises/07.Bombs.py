def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


def explode(row, col, size, matrix):
    bomb = matrix[row][col]
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if is_valid(i, j, size) and matrix[i][j] > 0:
                matrix[i][j] -= bomb


n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])

line = input().split()

for coordinates in line:
    tokens = [int(x) for x in coordinates.split(",")]
    row = tokens[0]
    col = tokens[1]
    if matrix[row][col] > 0:
        explode(row, col, n, matrix)
        matrix[row][col] = 0

alive_cells = 0
sum_alive_cells = 0

for r in range(n):
    for c in range(n):
        if matrix[r][c] > 0:
            sum_alive_cells += matrix[r][c]
            alive_cells += 1
print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_alive_cells}")
for row in matrix:
    print(' '.join([str(x) for x in row]))
