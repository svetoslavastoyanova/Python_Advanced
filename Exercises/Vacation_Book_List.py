page_counts = int(input())
pages_per_hour = int(input())
day_counts = int(input())

total_time = page_counts/pages_per_hour
day_counts = total_time/day_counts

print(day_counts)