data = input().split(", ")
filtered_data = {x: len(x) for x in data}
final_list = []
for key, value in filtered_data.items():
    final_list.append(f"{key} -> {value}")
print(', '.join(final_list))


