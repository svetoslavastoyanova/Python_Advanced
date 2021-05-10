n = int(input())
matrix = []
for _ in range(n):
    data = input().split(", ")
    matrix.append(data)

first_diagonal = [matrix[i][i] for i in range(len(matrix))]
second_diagonal = [matrix[i][len(matrix)-1-i] for i in range(len(matrix))]
print(f"First diagonal: {', '.join(first_diagonal)}. Sum: {sum(map(int, first_diagonal))}")
print(f"Second diagonal: {', '.join(second_diagonal)}. Sum: {sum(map(int, second_diagonal))}")