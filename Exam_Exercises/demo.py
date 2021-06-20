def numbers_searching(*args):
    final_list = []
    number = 0
    all_nums = list(set(args))
    missing_number = [x for x in range(all_nums[0], all_nums[-1]+1) if x not in all_nums]
    for n in missing_number:
        number = n
    final_list.append(number)
    duplicates = []
    none_duplicates = []
    for num in args:
        if num in none_duplicates:
            duplicates.append(num)
        else:
            none_duplicates.append(num)
    set_of_duplicates = set(duplicates)
    final_list.append(list(sorted(set_of_duplicates)))
    return final_list






print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))