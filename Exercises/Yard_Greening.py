yard_size = float(input())

total_price = yard_size * 7.61
discount = total_price * 0.18
total_price = total_price - discount
print(f'The final price is: {total_price} lv.')
print(f'The discount is: {discount} lv.')