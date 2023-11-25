#1.3
def is_perfect(n):
    counter=0
    for i in range(1,n):
        if n%i==0:
            counter+=i
    if counter==n:
        return True
    else: 
        return False  
def is_prime(n):
    counter=0
    for i in range(1,n+1):
        if n%i==0:
            counter+=1
    if counter==2:
        return True
    else: 
        return False 
def special_sum(n):
    sum=0
    for i in range(n+1):
        if is_perfect(i)==True or is_prime(i)==True:
            sum+=i
    return sum

print(special_sum(int(input(''))))           
#Write a function called special_sum that calculates the sum 
# of all numbers that are either prime numbers or perfect up till 
# the integer value given in its parameter. This integer value must be 
# taken as user input and passed into the function.													