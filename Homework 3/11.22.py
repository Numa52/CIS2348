#Ryan Nguyen PSID: 1805277

#taking input from the user
words = input().split()

#for loop to go through input
for word in words:
#base for counter
    count = 0
    for w in words:
        if w == word:
        #counting each time loop is going played
            count += 1
    print(word,count)
