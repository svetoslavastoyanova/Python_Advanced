from collections import deque
first_player, second_player = [x for x in input().split(', ')]
matrix = [list(input().split(' ')) for _ in range(7)]
p = [first_player, second_player]
players = deque(p)
won = False
winner = ""
scores = {
    f"{first_player}": 501,
    f"{second_player}": 501,
}
throws = {
    f"{first_player}": 0,
    f"{second_player}": 0,
}

while True:
    command = input().strip('(')
    command = command.strip(')')
    position_p = tuple(map(int, command.split(',')))
    row = position_p[0]
    col = position_p[1]
    current_player = players.popleft()
    throws[current_player] += 1

    if not 0 <= row < len(matrix) or not 0 <= col < len(matrix):
        continue
    if matrix[row][col].isdigit():
        scores[current_player] -= int(matrix[row][col])
    if matrix[row][col] == "B":
        won = True
        winner = current_player
        break
    if matrix[row][col] == "D":
        sum = 0
        left_num = int(matrix[row][0])
        right_num = int(matrix[row][6])
        bottom_num = int(matrix[6][col])
        upper_num = int(matrix[0][col])
        sum += (left_num+right_num+bottom_num+upper_num)*2
        scores[current_player] -= sum
    if matrix[row][col] == "T":
        sum = 0
        left_num = int(matrix[row][0])
        right_num = int(matrix[row][6])
        bottom_num = int(matrix[6][col])
        upper_num = int(matrix[0][col])
        sum += (left_num + right_num + bottom_num + upper_num) * 3
        scores[current_player] -= sum

    players.append(current_player)

    for key, value in scores.items():
        if value <= 0:
            won = True
            winner = current_player
            break

points = throws[winner]
print(f"{winner} won the game with {points} throws!")





