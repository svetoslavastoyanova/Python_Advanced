from collections import deque
list_of_customers = deque([int(x) for x in input().split(", ")])
list_of_taxis = deque([int(x) for x in input().split(", ")])
total_time = 0
while list_of_customers:
    if not list_of_taxis:
        final_list_customers = list(map(str, list_of_customers))
        print(f"Not all customers were driven to their destinations")
        print(f"Customers left: {', '.join(final_list_customers)}")
        break
    first_customer = list_of_customers.popleft()
    last_taxi = list_of_taxis.pop()

    if last_taxi >= first_customer:
        total_time += first_customer
    else:
        list_of_customers.appendleft(first_customer)

if not list_of_customers:
    print(f"All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")


