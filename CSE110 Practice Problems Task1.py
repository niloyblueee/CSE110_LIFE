#Check if a number is even. 
#If it is even, also check if it is a multiple of 3 and 5. 
#If it is, print ‘Even and a multiple of 3 and 5’. 
#Else if it is even but a multiple of 3 only, print,
# ‘Even and a multiple of 3’. 
#Else if it is even but a multiple of 5 only, print,
# ‘Even and a multiple of 5’. 
#Else, print, ‘Even but not a multiple of 3 or 5’
#But if the number is odd, print, ‘The number is odd’


num=int(input(""))
if num%2==0:


    if num%3==0:
        if num%5==0:
            print('Even and and a multiple of both 3 and 5')
        else:
            print('Even and a multiple of 3')
    elif num%5==0:
        print('even and a multiple of 5')    
    else:
        print('even and not a multipe of 3 and 5')
else:
    print("The number is odd")



