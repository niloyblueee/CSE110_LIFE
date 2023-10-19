#Take a range from the user and print if any
 #number is prime from 1 to that range

a=int(input("the range "))
for num in range(1,a+1):
    count=0
    for i in range (1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print(num,"prime")