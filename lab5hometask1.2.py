def is_perfect(n):
    counter=0
    for i in range(1,n):
        if n%i==0:
            counter+=i
    if counter==n:
        return True
    else: 
        return False  


perfect_check = is_perfect(8128)
print(perfect_check)

#perfect checker by function