cake_price = 45
waffles_price = 5.80
pancake_price = 3.20


day_counts = int(input())
bakers_count = int(input())
cake_counts = int(input())
waffles_count = int(input())
pancakes_count = int(input())

daily_wage = (cake_price*cake_counts + waffles_price*waffles_count + pancake_price*pancakes_count) * bakers_count
total_sum = daily_wage*day_counts
charity_money = total_sum - 1/8*total_sum
print(charity_money)


