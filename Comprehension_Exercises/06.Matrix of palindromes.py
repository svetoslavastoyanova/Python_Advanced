rows, cols = [int(x) for x in input().split()]
matrix = [[f"{chr(rows)}{chr(rows+cols)}{chr(rows)}" for cols in range(cols)]for rows in range(97, 97 + rows)]

[print(' '.join(rows)) for rows in matrix]