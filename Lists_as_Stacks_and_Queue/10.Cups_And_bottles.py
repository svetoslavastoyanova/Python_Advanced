from collections import deque
wasted_water = 0
cups_capacity = deque(map(int, input().split()))
filled_bottles = deque(map(int, input().split()))

while True:
    if not filled_bottles or not cups_capacity:
        break
    last_bottle = filled_bottles.pop()
    first_entered_cup = cups_capacity.popleft()

    if first_entered_cup <= last_bottle:
        wasted_water += last_bottle - first_entered_cup
        first_entered_cup -= last_bottle
    if first_entered_cup > last_bottle:
        while first_entered_cup > 0:
            first_entered_cup = first_entered_cup - last_bottle
            if first_entered_cup <= 0 and last_bottle > 0:
                wasted_water += abs(first_entered_cup)
            else:
                last_bottle = filled_bottles.pop()
            if not filled_bottles:
                break
if filled_bottles:
    joined_bottles = ' '.join(map(str, filled_bottles))
    print(f"Bottles: {joined_bottles}")
if cups_capacity:
    joined_cups = ' '.join(map(str, cups_capacity))
    print(f"Cups: {joined_cups}")
print(f"Wasted litters of")
print(f"water: {wasted_water}")