data = input()
phonebook = {}
nums = 0
while True:
    if "-" not in data:
        nums = int(data)
        break
    information = data.split("-")
    name = information[0]
    number = information[1]
    if name not in phonebook:
        phonebook[name] = number
    else:
        phonebook[name] = number
    data = input()
for i in range(nums):
    names = input()
    if names not in phonebook.keys():
        print(f"Contact {names} does not exist.")
    else:
        print(f"{names} -> {phonebook[names]}")

