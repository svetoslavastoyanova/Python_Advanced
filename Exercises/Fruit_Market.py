strawberries_price = float(input())


bananas_weight = float(input())
oranges_weight = float(input())
raspberries_weight = float(input())
strawberries_weight = float(input())


raspberries_price = 1/2*strawberries_price
oranges_price = 0.6*raspberries_price
bananas_price = 0.2*raspberries_price

total_price = (strawberries_price*strawberries_weight + oranges_price*oranges_weight +
               bananas_price*bananas_weight +raspberries_price*raspberries_weight)

print(total_price)