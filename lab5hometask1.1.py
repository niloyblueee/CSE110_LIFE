def is_prime(n):
    counter=0
    for i in range(1,n+1):
        if n%i==0:
            counter+=1
    if counter==2:
        return True
    else: 
        return False  


prime_check = is_prime(8)
print(prime_check)

#prime checker by function
