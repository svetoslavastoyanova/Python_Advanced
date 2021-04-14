def flights(*args):
    info = {}
    for i in range(0, len(args), 2):
        key = str(args[i])
        if key == "Finish":
            break
        else:
            value = int(args[i + 1])
            if key not in info:
                info[key] = value
            else:
                info[key] += value
    return info




print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))