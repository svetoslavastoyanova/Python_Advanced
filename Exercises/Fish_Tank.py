lenght = int(input())
width = int(input())
height = int(input())
volume = float(input())

total_volume = lenght*width*height
liters = total_volume*0.001
percent = volume*0.001
total_water = liters - percent*liters

print(total_water)






