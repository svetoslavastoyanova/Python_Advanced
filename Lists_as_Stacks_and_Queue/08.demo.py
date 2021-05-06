from collections import deque

price_of_bullet = int(input())
size_of_gun_barrel = int(input())
bullets = deque(map(int, input().split()))
locks = deque(map(int, input().split()))
value_of_the_intelligence = int(input())
used_bullets = 0
while True:
    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    if current_bullet <= current_lock:
        print("Bang!")
    else:
        locks.appendleft(current_lock)
        print("Ping!")
    used_bullets += 1
    if not locks:
        bullets_cost = used_bullets * price_of_bullet
        money_earned = value_of_the_intelligence - bullets_cost
        if bullets:
            if used_bullets % size_of_gun_barrel == 0:
                print(f"Reloading!")
        print(f"{len(bullets)} bullets left. Earned ${money_earned}")
        break
    if bullets:
        if used_bullets % size_of_gun_barrel == 0:
            print(f"Reloading!")
    else:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break





