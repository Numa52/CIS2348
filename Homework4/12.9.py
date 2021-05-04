#Ryan Nguyen PSID: 1805277

#splitting input into 2 different parts 1) Name and 2) Age
parts = input().split()
name = parts[0]
#while loop for age
while name != '-1':
    try:
        age = int(parts[1]) + 1
    except Exception as ex:
        age = 0
    # Get next line
    print('{} {}'.format(name, age))
    parts = input().split()
    name = parts[0]