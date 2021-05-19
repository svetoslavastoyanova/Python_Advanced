def age_assignment(*args, **kwargs):
    data = {}
    for w in args:
        first_letter = w[0]
        data[w] = 0
        for key, value in kwargs.items():
            if key == first_letter:
                data[w] = value
    return data





print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))