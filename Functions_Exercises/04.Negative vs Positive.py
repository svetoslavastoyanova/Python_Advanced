def negative_num(nums):
    return filter(lambda x: x < 0, nums)


def positive_num(nums):
    return filter(lambda x: x > 0, nums)


numbers = list(map(int, input().split()))
positive_numbers = sum(positive_num(numbers))
negative_numbers = sum(negative_num(numbers))
print(negative_numbers, positive_numbers, sep="\n")
if abs(negative_numbers) > positive_numbers:
    print(f"The negatives are stronger than the positives")
else:
    print(f"The positives are stronger than the negatives")
