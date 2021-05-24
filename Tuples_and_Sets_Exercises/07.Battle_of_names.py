n = int(input())
odd_set = set()
even_set = set()
for i in range(1, n + 1):
    names = input()
    summed_ascii = sum([ord(x) for x in names]) // i

    if summed_ascii % 2 == 0:
        even_set.add(summed_ascii)
    else:
        odd_set.add(summed_ascii)

odd_sum = sum(odd_set)
even_sum = sum(even_set)

if odd_sum == even_sum:
    union = odd_set.union(even_set)
    print(', '.join(map(str, union)))
elif odd_sum > even_sum:
    diff_values = odd_set.difference(even_set)
    print(', '.join(map(str, diff_values)))
else:
    symetric = odd_set.symmetric_difference(even_set)
    print(', '.join(map(str, symetric)))
