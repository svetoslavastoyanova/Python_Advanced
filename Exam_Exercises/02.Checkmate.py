def catch_king(row, matrix, curent_pos):
    current_row = curent_pos[0]
    current_col = curent_pos[1]




rows = 8
matrix = []
for _ in range(rows):
    data = input().split()
    matrix.append(data)
king_position = []
for i in range(rows):
    for j in range(rows):
        if matrix[i][j] == "K":
            king_position = [i, j]

for i in range(rows):
    for j in range(rows):
        if matrix[i][j] == "Q":
            current_queen_position = [i, j]
            catch_king(rows, matrix, current_queen_position)

print(king_position)
print(matrix)