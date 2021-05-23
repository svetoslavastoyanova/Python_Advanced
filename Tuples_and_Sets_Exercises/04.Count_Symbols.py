text = input()
characters = {}

for ch in text:
    if ch not in characters:
        characters[ch] = 0
    characters[ch] += 1

for key, value in sorted(characters.items()):
    print(f"{key}: {value} time/s")