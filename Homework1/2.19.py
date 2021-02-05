#Ryan Nguyen PSID: 1805277

#asking for ingredients
lemon_juice = int(input("Enter amount of lemon juice (in cups):\n"))
water = int(input("Enter amount of water (in cups):\n"))
agave_nector = float(input("Enter amount of agave nectar (in cups):\n"))
servings = int(input("How many servings does this make?\n"))
print("")

#printing inputs
print("Lemonade ingredients - yields",('{:.2f}'.format(servings)), "servings")
print('{:.2f}'.format(lemon_juice), "cup(s) lemon juice")
print('{:.2f}'.format(water), "cup(s) water")
print('{:.2f}'.format(agave_nector), "cup(s) agave nectar")
print("")

#asking for amount of servings
#(cups*desired_servings)/servings to get calculated ingredients
desired_servings = int(input("How many servings would you like to make?\n\n"))
print("Lemonade ingredients - yields",('{:.2f}'.format(desired_servings)), "servings")
print('{:.2f}'.format((lemon_juice * desired_servings / servings)), "cup(s) lemon juice")
print('{:.2f}'.format((water * desired_servings / servings)), "cup(s) water")
print('{:.2f}'.format((agave_nector * desired_servings / servings)), "cup(s) agave nectar\n")

#converting cups to gallons
print("Lemonade ingredients - yields",('{:.2f}'.format(desired_servings)), "servings")
print('{:.2f}'.format((lemon_juice * desired_servings / servings) / 16), "gallon(s) lemon juice")
print('{:.2f}'.format((water * desired_servings / servings) / 16), "gallon(s) water")
print('{:.2f}'.format((agave_nector * desired_servings / servings) / 16), "gallon(s) agave nectar")


