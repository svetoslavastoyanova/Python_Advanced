first = input()
second = input()


def get_characters_in_range(first, second):
    result = ""
    for i in range(ord(first)+1, ord(second)):
        result += chr(i) + " "

    return result

print(get_characters_in_range(first, second))


