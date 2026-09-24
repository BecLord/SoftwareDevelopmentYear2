#import random - to pick a random player
#import time to pause the game for 30 seconds
#Create an empty list - players
#asks the user to enter 12 players useing a while loop and add them to the list of players
#make a copy of the players to show at the end after eliminations - player.copy()
#ask user to pick a number of players to eliminate - input()
#for loop to eliminate the players
#uses random to pick a index from the player list
#remove (pop) the play at that index
#waits 30 seconds before next elimination - time.sleep()
#show the remaining players as a tuple - players()
#show the original list of players - players.copy()
#Lecture notes, GeeksforGeek - list, random module, tuples, time sleep method

import random
import time

players = []
print("Enter 12 player names for the game")

while len(players) < 12:
    name = input("What's the name for player " + str(len(players)+1) + "?")
    players.append(name)

list_of_players = players.copy()

while True:
    number_of_eliminations = input("Pick a number from 2 to 6 to eliminate that many players: ")
    try:
        number_of_eliminations = int(number_of_eliminations)
        if number_of_eliminations >= 2 and number_of_eliminations <= 6:
            break
        else:
            print("Please pick a number between 2 and 6")
    except:
        print("Please enter a number between 2 and 6")

for i in range(number_of_eliminations):
    if len(players) == 0:
        print("No players to eliminate")
        break
    place_in_list = random.randint(0, len(players) -1)
    eliminated = players.pop(place_in_list)
    print(eliminated + "! Has been eliminated")
    if i != number_of_eliminations -1:
        print("Wait for next elimination")
        time.sleep(30)

print("\nSurvivors")
print(tuple(players))

print("\nList of Players")
print(list_of_players)
