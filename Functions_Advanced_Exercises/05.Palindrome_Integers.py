numbers = input().split(", ")


def is_palindrome(numbers):
    result = ""
    for i in range(len(number) -1, -1, -1):
        result += number[i]
    return result == number

for number in numbers:
    print(is_palindrome(numbers))
