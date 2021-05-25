rows, cols = [int(x) for x in input().split()]
matrix = []
counter = 0
for _ in range(rows):
    line = [el for el in input().split()]
    matrix.append(line)

for i in range(rows-1):
    for j in range(cols-1):
        current_element = matrix[i][j]
        next_element_same_row = matrix[i][j+1]
        bottom_element = matrix[i+1][j]
        bottom_element_right = matrix[i+1][j+1]
        if current_element == next_element_same_row and next_element_same_row == bottom_element and bottom_element == bottom_element_right:
            counter += 1

print(counter)