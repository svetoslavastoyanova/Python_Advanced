clothes = list(map(int, input().split()))
rack_capacity = int(input())
counter_racks = 1
current_capacity = rack_capacity
while clothes:
    current_clothes = clothes.pop()
    if current_clothes <= current_capacity:
        current_capacity -= current_clothes
    else:
        counter_racks += 1
        current_capacity = rack_capacity
        current_capacity -= current_clothes

print(counter_racks)
