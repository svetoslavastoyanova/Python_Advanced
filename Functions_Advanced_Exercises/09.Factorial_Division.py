n1 = int(input())
n2 = int(input())


def factorial_of_first(n1):
     return 1 if (n1 == 1 or n1 == 0) else n1 * factorial_of_first(n1 - 1)

def factorial_of_second(n2):
    return 1 if (n2 == 1 or n2 == 0) else n2 * factorial_of_second(n2 - 1)

print(f"{factorial_of_first(n1)/factorial_of_second(n2):.2f}")




