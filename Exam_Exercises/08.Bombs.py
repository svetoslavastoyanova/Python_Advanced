from collections import deque
bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casing = deque([int(x) for x in input().split(", ")])
bomb_table = {
    "Datura Bombs": 40,
    'Cherry Bombs': 60,
    "Smoke Decoy Bombs": 120,
}
created_bombs = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0,
}
more_than_three_bombs = 0
while True:
    if not bomb_casing or not bomb_effects:
        break
    if more_than_three_bombs == 3:
        break
    first_bomb_effect = bomb_effects.popleft()
    last_bomb_casing = bomb_casing.pop()
    result = first_bomb_effect+last_bomb_casing
    if result in bomb_table.values():
        searched_value = result
        for key, value in bomb_table.items():
            if value == searched_value:
                searched_key = key
                created_bombs[searched_key] += 1
                if created_bombs[searched_key] == 3:
                    more_than_three_bombs += 1

    else:
        bomb_effects.appendleft(first_bomb_effect)
        bomb_casing.append(last_bomb_casing)
        index_casing = bomb_casing.index(last_bomb_casing)
        bomb_casing[index_casing] -= 5





result = 0
for key, value in created_bombs.items():
    if value != 0:
        result += 1
if result == 3:
    print(f"Bene! You have successfully filled the bomb pouch!")
else:
    print(f"You don't have enough materials to fill the bomb pouch.")
if not bomb_effects:
    print(f"Bomb Effects: empty")
else:
    bombs = ", ".join(list(map(str, bomb_effects)))
    print(f"Bomb Casings: {bombs}")
if not bomb_casing:
    print(f"Bomb Casings: empty")
else:
    casings = ', '.join(list(map(str, bomb_casing)))
    print(f"Bomb Effects: {casings}")
for key, value in sorted(created_bombs.items()):
    print(f"{key}: {value}")



print(more_than_three_bombs)