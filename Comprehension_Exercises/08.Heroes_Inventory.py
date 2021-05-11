collection = {name: {} for name in input().split(", ")}

data = input()
while data != "End":
    tokens = data.split("-")
    name = tokens[0]
    item = tokens[1]
    price = int(tokens[2])
    if item not in collection[name]:
        collection[name][item] = price
    data = input()
[print(f"{name} -> Items: {len(collection[name])}, Cost: {sum(collection[name].values())}") for name in collection]