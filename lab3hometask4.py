n=int(input('quantity: '))
max=0
min=0
storage=0
avg=0
for inputs in range (n):
    n2=int(input(""))
    if 0>n2 or n2>=max:
        max=n2
    elif 0<n2 or 0<=min:
         min=n2  
    storage+=n2     
avg=storage/n       
print('Maximum',max) 
print('Minimum',min) 
print('Average is',avg)

#Write a Python program that asks the user for a quantity,
#then takes that many numbers as input and prints the maximum, 
#minimum and average of those numbers.

