numbers = map(int, input().split())
even_nums = filter(lambda x: x % 2 == 0, numbers)
print(list(even_nums))