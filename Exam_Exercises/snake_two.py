def snake_movements(n, matrix, snake_position, food):
    food = 0
    old_row = snake_position[0]
    old_col = snake_position[1]
    new_position_up = [old_row-1][old_col]
    new_position_down = [old_row+1][old_col]
    new_position_right = [old_row+1][old_col+1]
    new_position_left = [old_col-1][old_row-1]
    if command == "up":
        pass

    elif command == "down":
        pass
    elif command == "right":
        pass
    elif command == "left":
        matrix[old_row][old_col] = "-"
        snake_position = new_position_left

        matrix[new_position_left] = "S"






n = int(input())
matrix = [list(input()) for _ in range(n)]
food_quantity = 0
snake_position = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] == "S":
            snake_position = [i, j]

while True:
    command = input()
    row = snake_position[0]
    col = snake_position[1]
    if matrix[row][col] == "B":
        pass
    snake_movements(n, matrix, snake_position, food_quantity)
