initial_string = input()
size = int(input())
matrix = []
player_position = []
for i in range(size):
    data = [x for x in input()]
    matrix.append(data)
for i in range(size):
    for j in range(size):
        if matrix[i][j] == "P":
            player_position = [i, j]

number_of_commands = int(input())
for number in range(number_of_commands):
    next_position = []
    command = input()
    if command == "up":
        next_position = [player_position[0]-1, player_position[1]]
    elif command == "down":
        next_position = [player_position[0] + 1, player_position[1]]
    elif command == "right":
        next_position = [player_position[0], player_position[1]+1]
    elif command == "left":
        next_position = [player_position[0], player_position[1]-1]

    if 0 <= next_position[0] < len(matrix) and 0 <= next_position[1] < len(matrix):
        row = next_position[0]
        col = next_position[1]
        if matrix[row][col] != "-":
            initial_string += matrix[row][col]
            matrix[player_position[0]][player_position[1]] = "-"
            matrix[row][col] = "P"
            player_position = next_position
        elif matrix[row][col] == "-":
            matrix[player_position[0]][player_position[1]] = "-"
            matrix[row][col] = "P"
            player_position = next_position

    else:
        if initial_string:
            initial_string = initial_string[:-1]

print(initial_string)
for row in matrix:
    print(''.join(row))