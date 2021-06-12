from collections import deque
males = deque([int(x) for x in input().split()])
females = deque([int(x) for x in input().split()])
matches_count = 0
while males or females:
    for female in females:
        if females[female] <= 0:
            females.remove(female)
        if female % 25 == 0:
            first_to_remove = females.index(female)
            next_to_remove = females.index(first_to_remove+1)
            females.pop(first_to_remove)
            females.pop(next_to_remove)

    for male in males:
        if males[male] <= 0:
            males.remove(male)
        if male % 25 == 0:
            first_to_remove = males.index(male)
            next_to_remove = males.index(first_to_remove + 1)
            males.pop(first_to_remove)
            males.pop(next_to_remove)

    first_female = females.popleft()
    last_male = males.pop()
    if first_female == last_male:
        matches_count += 1
    else:
        males.append(last_male)
        males[last_male] -= 2
    if not males or not females:
        break

print(f"Matches: {matches_count}")
if males:
    print(f"Males left: {len(males)}")
else:
    print(f"Males left: none")
if females:
    print(f"Females left: {len(females)}")
else:
    print(f"Females left: none")