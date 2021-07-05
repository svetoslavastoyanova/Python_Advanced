number = int(input())


def is_perfect(number):
    divisiors = []
    for i in range(1,  number):
        if number % i == 0:
            divisiors.append(i)
    return sum(divisiors) == number

if is_perfect(number):
    print(f"We have a perfect number!")
else:
    print(f"It's not so perfect.")