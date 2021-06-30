text = input()


def odd_even_sum_text(text):
    odd_sum = 0
    even_sum = 0

    for i in text:
        number = int(i)
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"

print(odd_even_sum_text(text))
