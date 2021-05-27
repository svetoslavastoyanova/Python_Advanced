rows, cols = [int(x) for x in input().split()]
matrix = []
for _ in range(rows):
    data = input().split()
    matrix.append(data)


line = input()
while line != "END":
    command = line.split()[0]
    if command == "swap" and len(line.split()) == 5:
        row_one = int(line.split()[1])
        col_one = int(line.split()[2])
        row_two = int(line.split()[3])
        col_two = int(line.split()[4])
        if 0 <= row_one < rows and 0 <= row_two < rows and 0 <= col_one < cols and 0 <= col_two < cols:
            matrix[row_one][col_one], matrix[row_two][col_two] = matrix[row_two][col_two], matrix[row_one][col_one]
            for row in matrix:
                print(' '.join(row))
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
    line = input()
