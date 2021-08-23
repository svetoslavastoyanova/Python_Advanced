table_counts = int(input())
table_lenght = float(input())
table_width = float(input())

tablecloth_area = table_counts * (table_lenght + 2*0.30) * (table_width + 2*0.30)
square_area = table_counts * (table_lenght/2) * (table_lenght/2)

tablecloth_price = tablecloth_area * 7
square_price = square_area * 9

usd = tablecloth_price + square_price
bgn = usd * 1.85

print(f'{usd: .2f}')
print(f'{bgn: .2f}')
