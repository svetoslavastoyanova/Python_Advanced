numbers = list(map(int, input().split()))
n = numbers[0]
m = numbers[1]
set_one = set()
set_two = set()
for _ in range(n):
    nums = int(input())
    set_one.add(nums)
for _ in range(m):
    nums = int(input())
    set_two.add(nums)

numbers = set_two & set_one
print('\n'.join(map(str, numbers)))