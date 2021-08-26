puzzle_price = 2.60
dall_price = 3
bear_price = 4.10
minion_price = 8.20
truck_price = 2

trip_price = float(input())
puzzle_counts = int(input())
dall_counts = int(input())
bear_counts = int(input())
minion_counts = int(input())
truck_counts = int(input())

toys_counts = puzzle_counts + dall_counts + bear_counts + minion_counts + truck_counts

income = puzzle_counts*puzzle_price + dall_counts*dall_price + bear_counts*bear_price + minion_counts*minion_price + truck_counts*truck_price

if toys_counts >= 50:
    income = income - (income*0.25) # income -= income*0.25
income = income - (income * 0.10) # income -= income*0.10
# income = income*0.75 ( izwadili sme 25% ot 100: 100-25% = 75%)
# income = income*0.90 (izwajdame 10% ot 100: 100 - 10 = 90(0.90)

if income >= trip_price:
#money_left = income - trip_price
    print(f'Yes! {income - trip_price:.2f} lv left.')
# print (money_left)...
else:
    income <= trip_price
#money_needed = trip_price - income (wadim taka, ako moite pari sa po-malki ot tezi za ekskyrziqta)
    print(f'Not enough money! {trip_price - income:.2f} lv needed.')
#print(money_needed)


