n = int(input())
counter = 0
stack = []
while counter != n:
    data = input().split()
    command = int(data[0])

    if command == 1:
        stack.append(int(data[1]))
    elif command == 2:
        if stack:
            stack.pop()
    elif command == 3:
        if stack:
            print(max(stack))
    elif command == 4:
        if stack:
            print(min(stack))
    counter += 1

print(', '.join(map(str, reversed(stack))))
