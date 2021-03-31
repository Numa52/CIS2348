#Ryan Nguyen PSID: 1805277

def printRoster():
   #getting player jersey numbers
   keys = list(players.keys())
   #sorting numbers in ascending order
   keys.sort()

   #printing the roster
   print("ROSTER")
   for key in keys:
       print("Jersey number: %d, Rating: %d" %(key,players[key]))

#creating a dictionary to store player jeresy numbers and raings
players = {}

#iterate for loop 5 times
for i in range(5):
    #ask for user to enter players jersey number
    jersey_num = int(input("Enter player %d's jersey number:\n" %(i+1)))
    #asking for user to enter player's rating
    players[jersey_num] = int(input("Enter player %d's rating:\n" % (i + 1)))
    print("")

printRoster()

#iterate while loop
while True:

    #print menu
    print(
        "\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n")

    #read user option
    option = input("Choose an option:\n")

    #if user option is o c all printRoster() function
    if option == "o":
        printRoster()

    #if user option is a change jersey number and ratings
    elif option == "a":
        jersey_num = int(input("Enter a new player's jersey number:\n"))
        rating = int(input("Enter the player's rating:\n"))
        players[jersey_num] = rating

    elif option =="d":
        #ead a player's jersey number
        jersey_num = int(input("Enter a player's jersey number: \n"))
        #check a player with the given jersey number is present in the dictionary
        if jersey_num in list(players.keys()):
            #delete player
            del players[jersey_num]

        #if user option is 'u'
    elif option == 'u':
        #read a player's jersey number
        jersey_num = int(input("Enter a player's jersey number: \n"))

        #read new player's rating
        rating = int(input("Enter a new rating for player:\n"))

        #update player details into players dictionary
        players[jersey_num] = rating

    elif option == 'r':
        #read a rating
        rating = int(input("Enter a rating:\n"))

        #get all players jersey numbers
        keys = list(players.keys())

        #sort jersey numbers in ascending order
        keys.sort()

        #print players above given rating
        print("\nABOVE %d" % (rating))

        count = 0
        for key in keys:
        # print player's jersey number, and rating
            if (players[key] > rating):
                print("Jersey number: %d, Rating: %d" % (key, players[key]))

            # increment count by 1
            count += 1

# if no players have above given rating, print error message
        if (count == 0):
            print("No players found above %d rating" % (rating))

# if user option is q then stop the program
    if option == "q":
        break