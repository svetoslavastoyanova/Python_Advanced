n = int(input())
commands = input().split()
matrix = []
first_position = []
coals = 0
total_coals = 0
end = False
for i in range(n):
    row = input().split()
    matrix.append(row)
    if "s" in row:
        first_position = [i, row.index("s")]
    total_coals += row.count("c")

for command in commands:
    next_position = []
    if command == "up":
        next_position = [first_position[0] - 1, first_position[1]]
    elif command == "down":
        next_position = [first_position[0] + 1, first_position[1]]
    elif command == "right":
        next_position = [first_position[0], first_position[1]+1]
    elif command == "left":
        next_position = [first_position[0], first_position[1]-1]

    if 0 <= next_position[0] < len(matrix) and 0 < next_position[1] < len(matrix):
        row = next_position[0]
        col = next_position[1]
        if matrix[row][col] == "*":
            matrix[first_position[0]][first_position[1]] = "*"
            matrix[row][col] = "s"
            first_position = next_position
        elif matrix[row][col] == "e":
            print(f"Game over! ({row}, {col})")
            end = True
            break
        elif matrix[row][col] == "c":
            coals += 1
            if total_coals == coals:
                print(f"You collected all coals! ({row}, {col})")
                end = True
                break
            matrix[first_position[0]][first_position[1]] = "*"
            matrix[row][col] = "s"
            first_position = next_position
if not end:
    print(f"{total_coals} coals left. ({first_position[0]}, {first_position[1]})")