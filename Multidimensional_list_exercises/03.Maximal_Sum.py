rows, cols = [int(x) for x in input().split()]
matrix = []
best_sum = -99999
max_row, max_col = 0, 0

for _ in range(rows):
    data = [int(x) for x in input().split()]
    matrix.append(data)

for row in range(rows - 2):
    for col in range(cols - 2):
        score = sum(matrix[row][col:col+3]) + sum(matrix[row+1][col:col+3]) + sum(matrix[row+2][col:col+3])
        if score > best_sum:
            best_sum = score
            max_row, max_col = row, col

print(f"Sum = {best_sum}")
for r in range(max_row, max_row+3):
    print(*matrix[r][max_col:max_col+3])