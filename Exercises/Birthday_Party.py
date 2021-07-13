venue_rent = int(input())

cake_price = 0.2 * venue_rent
drinks_price = cake_price - 0.45 * cake_price
animator_price = 1/3 * venue_rent

total_sum = venue_rent + cake_price + drinks_price + animator_price

print(total_sum)