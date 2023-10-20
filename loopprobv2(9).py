winner1="PLayer 1"
winner2='Player 2'
sum1=0
sum2=0
while True:
    n1=int(input('PLayer 1: '))
    sum1+=n1
    n2=int(input('Player 2: '))
    sum2+=n2
    if sum1==25:
        print(winner1,'wins')
        break
    elif sum2==25:
        print(winner2,'wins')   
        break
print("THE END")

#9. Imagine you are playing a game with your friend which is quite similar to ludo. The player who crosses
#throughout the board of exactly 25 boxes wins. Each of you gets to roll the dice and can get from 1-6.
#If a player crosses 24 boxes, he/she has to get exactly 1 after rolling the dice in order to win. Otherwise, he/she
#will stay in the same place. The one who gets to the 25th box first will win.
#Until a winner is decided, the dice will be rolled between the players and the game will continue.
#Sample Input 1:
#Player 1: 6
#Player 2: 4
#Player 1: 5
#Player 2: 5
#Player 1: 6
#Player 2: 4
#Player 1: 4
#Player 2: 6
#Player 1: 3
#Player 2: 6
#Sample Output:
#Player 2 wins