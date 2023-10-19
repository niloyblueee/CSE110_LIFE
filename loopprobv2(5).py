count=0
prod=1
while True:
    n=input('enter number: ')
    if n=='STOP':
        prod=0
        break


    else:
        prod=prod*int(n)
        count+=1
print(prod)    

#Write a python program that takes integer 
# Inputs from the user until the user gives "STOP".
#  Print the product of all the numbers.
# Sample Input1:
#5
#6
#-02
#7
#2
#STOP
#Sample Output1:
#-840


    
