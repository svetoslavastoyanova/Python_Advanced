n = int(input())


def loading_bar(n):
    first = ("%"*int(n/10))
    second = ("."*int(10-n/10))
    loading_bar = first+second
    return loading_bar


if n == 100:
    print(f'100% Complete!\n[{loading_bar(n)}]')
else:
    print(f'{n}% [{loading_bar(n)}]\nStill loading...')