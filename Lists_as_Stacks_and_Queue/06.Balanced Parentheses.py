from collections import deque

parentheses = deque(input())
brackets = ["{, }", "(, )", "[, ]"]
while parentheses:
    left_ch = parentheses.popleft()+", "
    right_ch = parentheses.pop()
    to_check = left_ch+right_ch
    if to_check in brackets:
        continue
    else:
        break

if parentheses:
    print("NO")
else:
    print("YES")
