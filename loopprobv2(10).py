winner1="PLayer 1"
winner2='Player 2'  #didnt solve
sum1=0
sum2=0
while True:
    n1=int(input('PLayer 1: '))
    sum1+=n1
    n2=int(input('Player 2: '))
    sum2+=n2
    if sum1==sum2!=10 or sum1==sum2!=20:
        if sum1==sum2:
          print("player 1 died")
          print('playere 2 wins')
          break
        elif sum2==sum1:
          print("player 2 died")
          print('playere 1 wins')
          break
    

    if sum1==25:
        print(winner1,'wins')
        break
    elif sum2==25:
        print(winner2,'wins')   
        break
print("THE END")