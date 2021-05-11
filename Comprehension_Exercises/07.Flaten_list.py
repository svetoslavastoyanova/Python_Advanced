from itertools import chain
data = input()
numbers = ([x for x in data.split("|")[::-1]])
final_list = []
for el in numbers:
    new_num = el.split()
    final_list.append(new_num)
chained_nums = list(chain(*final_list))
print(" ".join(chained_nums))