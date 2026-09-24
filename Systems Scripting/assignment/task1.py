import random
import time
# Task 1
# Elimination Game, 12 players, during game randomy eliminate 2-6 players, 
# display the name of the player each time they are eliminated and 
# output the name then wait 30 seconds.

def elimination_game(players, rounds):
    if rounds >= 2 and rounds <= 6:
        count = 0
        while (count < rounds):
            count = count + 1
            print("Round " + str(count))
            eliminate = random.choice(players) #pick a random player
            players.remove(eliminate) #eliminate a player
            print("Player " + eliminate + " was eliminated") #display the player elimanated
            time.sleep(30) #wait 30 seconds
    
    print("After " + str(rounds) +" rounds, Here are the survivors!")
    print(players) #display all the players left (final list)
    print("Thanks for playing!")

print("Elimination Game")
players = ["u1", "John", "Mary", "Mike", "Lilly", "Bob", "James", "Ivy", "Sarah", "Cara", "Barry", "Cian"]
players[0] = input("What is your name? ")
originalPlayers = players.copy()

print("Hello " + players[0] + ", let's play the Elimination Game")

while True:
    try:
        rounds = int(input("How many rounds do you want to play (2-6)? "))
        if 2<= rounds <= 6:
            break
        else:
            print("Please enter a number between 2 & 6 ")
    except ValueError:
        print("Please enter a number")

result = elimination_game(players, rounds)
print("Result tuple", result)
print("Original list", originalPlayers)

# First I created a list of 12 players.
# Then i used input() to ask the user to enter their name and made them player[0], the first player in the game.
# I marked out the print statements like print("Please enter a number between 2 & 6") and added in comments like #if statement for number of players to eliminate (rounds)
# I then created an if statement to ask how many rounds were to be played to get the number of players to eliminate.
# I went back at then end when i realised we had to handle invalid input and added in a while loop with a try block to catch ValueError.
# I added in the random.choice function, to pick the players that would be eliminated each round, then I removed them from the list with .remove.
# I added in the time.sleep() at the end of the while loop to wait for 30 seconds after each round.
# I then made the code that eliminated a player into a while loop so that it would repeat for the number of rounds that the users had inputed.
# I put the code for picking and eliminating the players into a function.
# At the end I created a copy of the players list which I called originalPlayers to store the list of players that I had at the start before got removed during the game,
# and the results tuple to display the survious list at the end. 

# References
# BroCode - Python Full Course (Youtube)
# GeeksforGeeks = python tuples
# GeeksforGeeks = python random module
# GeeksforGeeks - python time module
