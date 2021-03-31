#Ryan Nguyen PSID: 1805277

#taking input from user
num_values = input()

#splitting numbers through spaces
list_values = [int(num) for num in num_values.split()
if int(num) > 0]

#Apply the sort() function over list of values to sort
#the values in ascending order.
list_values.sort()

#displaying result without negative numbers
for value in list_values:

    print(value, end = ' ')