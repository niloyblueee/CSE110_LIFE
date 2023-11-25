def reverse_digits(n):
    if n==0:
        return
    out=n%10
    n=n//10 
    print(out)
    reverse_digits(n)
    
    
reverse_digits(1000)


#Write a recursive function called reverse_digits
#  that takes an integer n as an argument and prints
#  the digits of n in reverse order.