import random

#Create two seperate lists for player one and player two. 

player1 = []
player2 = []

#Each one should contain 10 random numbers between 1 and 50.
#Do NOT sort the lists.

for i in range (10):
    player1.append(random.randrange(1, 50, 1))
    player2.append(random.randrange(1, 50, 1))


#Compare the lists in order. Whichever list has the higher number wins.
#Keep track of how many times each list wins.
#A tie is not record as a win for either player

player1_win = 0
player2_win = 0
noone_win = 0

for i in range(10):
    if player1[i] > player2[i]:
        player1_win += 1
    elif player1[i] < player2[i]:
        player2_win += 1
    else:
        noone_win += 1


#Find the highest number in each list and it's index. If the number occurs multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occurs multiple times take the first instsance.


player1_highest = max(player1)
player1_high_index = player1.index(player1_highest)
player1_lowest = min(player1)
player1_low_index = player1.index(player1_lowest)

player2_highest = max(player2)
player2_high_index = player2.index(player2_highest)
player2_lowest = min(player2)
player2_low_index = player2.index(player2_lowest)


#Display the lists

print(f"Player 1's record is {player1}")
print(f"Player 2's record is {player2}")


#Report to the user how many times each player won and the information from lines 6 and 7.

print(f"Player 1 won {player1_win} times.")
print(f"Player 2 won {player2_win} times.")
print(f"The players tied {noone_win} times.")
print(f"Player 1's highest number is {player1_highest}, and is at position {player1_high_index}. Player 1's lowest number is {player1_lowest} and is at position {player1_low_index}.")
print(f"Player 2's highest number is {player2_highest}, and is at position {player2_high_index}. Player 2's lowest number is {player2_lowest} and is at position {player2_low_index}.")
