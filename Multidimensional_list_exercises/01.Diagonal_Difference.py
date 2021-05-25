n = int(input())
first_sum = 0
second_sum = 0
rows = [[int(x) for x in input().split()] for _ in range(n)]
for i in range(len(rows)):
    first_diagonal = rows[i][i]
    first_sum += first_diagonal

for i in range(len(rows)):
    second_diagonal = rows[i][(len(rows)-1- i)]
    second_sum += second_diagonal
print(abs(first_sum-second_sum))