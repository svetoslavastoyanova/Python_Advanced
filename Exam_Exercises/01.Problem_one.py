from collections import deque

firework_effects = deque([int(x) for x in input().split(", ")])
explosive_power = deque([int(x) for x in input().split(", ")])

data = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0,
}
while True:
    if not explosive_power or not firework_effects:
        break
    if data["Palm Fireworks"] >= 3 and data["Willow Fireworks"] >= 3 and data["Crossette Fireworks"] >= 3:
        break
    first_firework = firework_effects.popleft()
    last_explosive = explosive_power.pop()
    if first_firework <= 0:
        explosive_power.append(last_explosive)
        continue
    if last_explosive <= 0:
        firework_effects.appendleft(first_firework)
        continue
    result = first_firework + last_explosive

    if result % 3 == 0 and result % 5 != 0:
        data["Palm Fireworks"] += 1
    elif result % 5 == 0 and result % 3 != 0:
        data["Willow Fireworks"] += 1
    elif result % 5 == 0 and result % 3 == 0:
        data["Crossette Fireworks"] += 1
    else:
        first_firework -= 1
        firework_effects.append(first_firework)
        explosive_power.append(last_explosive)

if data["Palm Fireworks"] >= 3 and data["Willow Fireworks"] >= 3 and data["Crossette Fireworks"] >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can’t make the perfect firework show.")

if firework_effects:
    fire = list(map(str, firework_effects))
    print(', '.join(fire))
if explosive_power:
    explosive = list(map(str, explosive_power))
    print(', '.join(explosive))
for key, value in data.items():
    print(f"{key}: {value}")