n = int(input())
first_range_set = set()
second_range_set = set()
intersections = []
for sets in range(n):
    intersection = 0
    data = input().split("-")
    first_range = data[0]
    second_range = data[1]
    numbers = first_range.split(",")
    first = int(numbers[0])
    second = int(numbers[1])
    for i in range(first, second + 1):
        first_range_set.add(i)
    numbers_two = second_range.split(",")
    third = int(numbers_two[0])
    fourth = int(numbers_two[1])
    for m in range(third, fourth + 1):
        second_range_set.add(m)

    intersection = first_range_set.intersection(second_range_set)
    intersections.append(intersection)
    first_range_set.clear()
    second_range_set.clear()

max_list = max(list((x) for x in intersections))
print(max_list)
print(len(max_list))
max_len = max(len(x) for x in intersections)
print(f"Longest intersection is {list(max_list)} with length {max_len}")
print(intersections)

