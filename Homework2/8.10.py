#Ryan Nguyen PSID: 1805277

user_input = input()
low = 0
high = len(user_input) - 1
result = True
while(low<high):
    if(user_input[low]== ' '):
        low+=1
    elif(user_input[high] == ' '):
        high-=1
    elif(user_input[low] != user_input[high]):
        result = False
        break
    else:
        low+=1
        high-=1
if (result):
    print(user_input, "is a palindrome")
else:
    print(user_input, "not a palindrome")