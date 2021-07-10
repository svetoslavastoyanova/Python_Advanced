whisky_price = float(input())
beer_amount = float(input())
wine_amount = float(input())
rakia_amount = float(input())
whisky_amount = float(input())

rakia_price = whisky_price / 2
wine_price = rakia_price - 0.4*rakia_price
beer_price = rakia_price - 0.8*rakia_price

whisky_sum = whisky_amount*whisky_price
beer_sum = beer_price * beer_amount
wine_sum = wine_price * wine_amount
rakia_sum = rakia_price * rakia_amount


total_sum = whisky_sum + beer_sum + wine_sum + rakia_sum
print(f' {total_sum: .2f} ')

