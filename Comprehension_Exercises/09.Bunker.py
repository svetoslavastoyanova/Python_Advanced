collection = {item_name: {} for item_name in input().split(", ")}
rows = int(input())
quantity_count = 0
quality_sum = 0
for i in range(rows):
    data = input().split(" - ")
    category = data[0]
    item_name = data[1]
    section_two = data[2].split(";")
    quantity = int(section_two[0].split(":")[1])
    quality = int(section_two[1].split(":")[1])
    collection[category][item_name] = [quantity, quality]
    quantity_count += quantity
    quality_sum += quality
print(f"Count of items: {quantity_count}")
print(f"Average quality: {quality_sum/len(collection):.2f}")
[print(f"{category} -> {', '.join(collection[category].keys())}") for category in collection]



