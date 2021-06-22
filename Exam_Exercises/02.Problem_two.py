import math
def is_in_range(col, row, n, matrix, command):
    if command == "up":
        if 0 <= row - 1 < len(matrix) and 0 <= col < len(matrix):
            return True
    if command == "down":
        if 0 <= row + 1 < len(matrix) and 0 <= col < len(matrix):
            return True
    if command == "right":
        if 0 <= row < len(matrix) and 0 <= col+1 < len(matrix):
            return True
    if command == "left":
        if 0 <= row < len(matrix) and 0 <= col - 1 < len(matrix):
            return True
    return False


n = int(input())
matrix = [list(input().split()) for _ in range(n)]
first_position = []
for i in range(n):
    for c in range(n):
        if matrix[i][c] == "P":
            first_position = [i, c]
row = first_position[0]
col = first_position[1]
coins = 0
positions = []
success = False
fail = False
while True:
    command = input()

    if not is_in_range(col, row, n, matrix, command):
        fail = True
        break

    if command == "up":
        if matrix[row-1][col] == "X":
            fail = True
            break
        else:
            if matrix[row-1][col].isdigit():
                number = matrix[row-1][col]
                coins += int(number)
                positions.append([row-1,col])
                row = row-1
                col = col

    elif command == "down":
        if matrix[row+1][col] == "X":
            fail = True
            break
        else:
            if matrix[row+1][col].isdigit():
                number = matrix[row+1][col]
                coins += int(number)
                positions.append([row+1,col])
                row = row + 1
                col = col

    elif command == "right":
        if matrix[row][col+1] == "X":
            fail = True
            break
        else:
            if matrix[row][col+1].isdigit():
                number = matrix[row][col+1]
                coins += int(number)
                positions.append([row,col+1])
                row = row
                col = col+1

    elif command == "left":
        if matrix[row][col-1] == "X":
            fail = True
            break
        else:
            if matrix[row][col-1].isdigit():
                number = matrix[row][col-1]
                coins += int(number)
                positions.append([row,col-1])
                row = row
                col = col-1
    if coins >= 100:
        success = True
        break

if success:
    print(f"You won! You've collected {coins} coins.")
    print("Your path: ")
    for position in positions:
        print(position)
else:
    coins *= 0.50
    print(f"Game over! You've collected {math.floor(coins)} coins.")
    print(f"Your path: ")
    for line in positions:
        print(f"{line}")
