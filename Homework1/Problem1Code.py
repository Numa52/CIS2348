print("This is a birthday Calculator")
#current day inputs
m1 = int(input("Please enter the current month(1-12): "))
d1 = int(input("Please enter the current day(1-31): "))
y1 = int(input("Please enter the current year: "))
#users birthday date input
print("Please enter your birthday date.")
m2 = int(input("Please enter your birth month(1-12): "))
d2 = int(input("Please enter your birth day(1-31): "))
y2 = int(input("Please enter your birth year: "))

years = y1-y2-1

if (m1==m2 and d1==d2):
    print("Happy birthday!")

print("You are", years, "years old.")
