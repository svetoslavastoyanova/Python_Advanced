data = [int(x) for x in input().split(", ")]
positive = [n for n in data if n >= 0]
negative = [n for n in data if n < 0]
even = [n for n in data if n % 2 == 0]
odd = [n for n in data if n % 2 != 0]
print(f"Positive: {', '.join(map(str, positive))}")
print(f"Negative: {', '.join(map(str, negative))}")
print(f"Even: {', '.join(map(str, even))}")
print(f"Odd: {', '.join(map(str, odd))}")