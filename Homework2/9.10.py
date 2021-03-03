#Ryan Nguyen PSID: 1805277
import csv

# user input for the file
fileName = input()

# dictionary to store words with their frequencies
wordsFrequency = {}

# reading the file
with open(fileName, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
# iterating throught each row
    for row in csvreader:
        for word in row:
# checking if word exixt in the dictionary or not if not present then add the word in the dictionary with frequency 1
            if word not in wordsFrequency.keys():
                wordsFrequency[word] = 1
# else increase the frequency by 1
            else:
                wordsFrequency[word] += 1

# printin the result
for key in wordsFrequency.keys():
    print(key + " " + str(wordsFrequency[key]))