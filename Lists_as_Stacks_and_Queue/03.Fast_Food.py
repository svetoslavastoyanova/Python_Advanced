from collections import deque

food_quantity = int(input())
orders = deque(map(int, input().split()))
print(max(orders))

while orders:
    current_order = orders.popleft()
    if current_order <= food_quantity:
        food_quantity -= current_order
    else:
        orders.appendleft(current_order)
        break

if not orders:
    print(f"Orders complete")
else:
    print(f"Orders left: {' '.join(map(str, orders))}")