from collections import deque


def best_list_pureness(list_of_nums, n):
    result_and_rotations = {}
    list_of_nums = deque([int(x) for x in list_of_nums])
    for rotations in range(n+1):
        result = 0
        list_of_nums.rotate(rotations)
        for index, num in enumerate(list_of_nums):
            result += index*num
        result_and_rotations[result] = rotations
    max_pureness = max([x for x in result_and_rotations.keys()])
    rotation_of_max = result_and_rotations[max_pureness]
    return f"Best pureness {max_pureness} after {rotation_of_max} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

