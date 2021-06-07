numbers = [int(x) for x in input().split(", ")]
needed_number_index = int(input())
clock_cycles = 0
data = {}
for index, num in enumerate(numbers):
    data[index] = num
sorted_data = sorted(data.items(), key=lambda x: -x[1], reverse=True)

for key, value in sorted_data:
    current_num = value
    current_index = key
    clock_cycles += current_num
    if current_index == needed_number_index:
        break

print(clock_cycles)
