data = input().split(" ")
filtered = [x for x in data if len(x) % 2 == 0]
print('\n'.join(filtered))