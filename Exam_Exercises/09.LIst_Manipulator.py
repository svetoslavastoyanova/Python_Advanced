def list_manipulator(list_of_nums, *args):
    third_parameter = None
    command = args[0]
    start_or_end = args[1]
    if args[2] in args:
        third_parameter = args[2]
        print('yes')
    else:
        print('no')
    return (command, start_or_end)


print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "add", "end", 30))