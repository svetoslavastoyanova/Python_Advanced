countries = input().split(", ")
capitals = input().split(", ")
zipped = dict(zip(countries, capitals))
# or filtered = {key:value for key, value in zipped}
for key, value in zipped.items():
    print(f"{key} -> {value}")