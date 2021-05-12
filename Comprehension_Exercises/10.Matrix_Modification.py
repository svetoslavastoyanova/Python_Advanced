rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
line = input()

while line != "END":
    data = line.split()
    command = data[0]
    row = int(data[1])
    cow = int(data[2])
    value = int(data[3])
    if 0 <= row < len(matrix) and 0 <= cow < len(matrix):
        if command == "Add":
            matrix[row][cow] += value
        elif command == "Subtract":
            matrix[row][cow] -= value
    else:
        print(f"Invalid coordinates")

    line = input()
[print(' '.join([str(x)for x in row])) for row in matrix]