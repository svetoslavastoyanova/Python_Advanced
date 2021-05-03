duration_green_light = int(input())
duration_of_free_window = int(input())
passed_cars = 0
line = input()
time = duration_green_light
entered_car = False
while line != "END":
    if time:
        if len(line) <= time:
            time -= len(line)
            passed_cars += 1
        else:
            left_characters = line[:time-1]
            ch_after_window = line[left_characters:]
            hit_character = line[0]

    if line == "green":
        entered_car = True
        time = duration_green_light
    else:
        if len(line) <= time:
            passed_cars += 1
            time -= len(line)
        else:
            hit_letter = line[time-1]
            if len(hit_letter) <= duration_of_free_window:
                passed_cars += 1
            else:
                hit_letter = line[duration_of_free_window]



    line = input()