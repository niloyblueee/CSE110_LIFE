def sequence_recursive(n):
    if n==1:
        return 1
    if n%2==0:
       return sequence_recursive(n-1)- n
       
    else:
        return sequence_recursive(n-1) + n
    

print(sequence_recursive(10))

#Write a recursive function called 
# sequence_recursive that calculates the value
#  of y if the expression of y is as follows 
#  (Here, N is the input)
#y = 1 - 2 + 3 - 4 + 5 - …… + N     