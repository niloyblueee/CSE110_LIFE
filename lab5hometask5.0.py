def sequence(n):
    sum=0
    for i in range(1,n+1):
        if i%2==0:
            sum-=i
        else:
            i%2!=0
            sum+=i 
    return sum

print(sequence(10))

#Write a function called sequence_iterative 
# that uses loop to calculate the value of y 
# if the expression of y is as follows  
# (Here, N is the input)
#y = 1 - 2 + 3 - 4 + 5 - …… + N       