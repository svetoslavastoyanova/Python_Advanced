from collections import deque

pizza_orders = deque([int(c) for c in input().split(', ')])
employees = list(map(int, input().split(", ")))
total_pizza_made = 0

while pizza_orders:
    if not employees:
        pizza_left = ', '.join(list(map(str, pizza_orders)))
        print(f"Not all orders are completed.")
        print(f"Orders left: {pizza_left}")
        break
    first_pizza = pizza_orders.popleft()
    last_employee = employees[-1]

    if first_pizza <= 0 or first_pizza > 10:
        continue

    if first_pizza <= last_employee:
        total_pizza_made += first_pizza
        employees.pop()
        continue

    if first_pizza > last_employee:
        first_pizza -= last_employee
        total_pizza_made += last_employee
        pizza_orders.appendleft(first_pizza)
        employees.pop()
        if not employees:
            pizza_left = ', '.join(list(map(str, pizza_orders)))
            print(f"Not all orders are completed.")
            print(f"Orders left: {pizza_left}")
            exit()
        last_employee = employees[-1]
        continue

print(f"All orders are successfully completed!")
print(f"Total pizzas made: {total_pizza_made}")
employees_left = ', '.join(list(map(str, employees)))
print(f"Employees: {employees_left}")