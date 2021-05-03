numbers = input().split(" ")
stack = []
while len(numbers) > 0:
    popped_number = numbers.pop()
    stack.append(popped_number)
print(' '.join(stack))


