def odd_nums(nums):
    return sum(filter(lambda x: x % 2 != 0, nums))


def even_nums(nums):
    return sum(filter(lambda x: x % 2 == 0, nums))


command = input()
numbers = list(map(int, input().split()))

if command == "Even":
    print(even_nums(numbers)*len(numbers))
elif command == "Odd":
    print(odd_nums(numbers)*len(numbers))