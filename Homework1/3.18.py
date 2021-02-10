#Ryan Nguyen PSID: 180527

#getting wall dimensions from user
wall_height = int(input("Enter wall height (feet):\n"))
wall_width = int(input("Enter wall width (feet):\n"))
wall_area = wall_width * wall_height
print("Wall area:", wall_area, "square feet")

#calculating gallons of paint needed
#1 gallon of paint covers 350 square feet
paint_needed = wall_area / 350
print("Paint needed:", '{:.2f}'.format(paint_needed), "gallons")
#rounding paint_needed to nearest whole to get # of cans needed
cans = round(paint_needed)
print("Cans needed:", cans, "can(s)\n")

#asking user for color selection
color = input("Choose a color to paint the wall:\n")

if (color == 'red'):
    cost = cans * 35
elif (color == 'blue'):
    cost = cans * 25
elif (color == 'green'):
    cost = cans * 23

#printing the final cost
print("Cost of purchasing", color, "paint: $" + str(cost))