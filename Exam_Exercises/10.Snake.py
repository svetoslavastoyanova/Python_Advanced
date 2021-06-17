def check_burrow(matrix, i, j):
    pass


n = int(input())
matrix = [list(input()) for _ in range(n)]
food_quantity = 0
snake_position = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] == "S":
            snake_position = [i, j]


command = input()
while food_quantity != 10:
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == "B":
                check_burrow(matrix, i, j)
            else:
                try:
                    if command == "up":
                        previous_position = snake_position[0][1]
                        snake_position = [snake_position[0]-1, snake_position[1]]

                    elif command == "down":
                        snake_position = [snake_position[0]+1, snake_position[1]]
                    elif command == "right":
                        snake_position = [snake_position[0]+1, snake_position[1]+1]
                    elif command == "left":
                        snake_position = [snake_position[0]-1, snake_position[1]-1]
                except:
                    break





    command = input()

