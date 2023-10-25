m=int(input('Total chocolate: '))  
n=int(input('Packets needed for new chocolates: ')) 
p=int(input('Amount of new chocolates: '))  
res1=m//n 
res2=m%n  
total=res1*p 
res3=total 
res4=total

sum=m+total 
while True:
    res1= (res4)//n 
    res2= res4%n
    total1=res1*p 
    res3=total1  
    res4=res3+res2
    sum+=total1 
    if res4<n:
        break
print('Total eaten chocolates:',sum)    

#You will be given three Inputs M, N, and P. M indicates the number of chocolates you have. And there is a shop
#where you can get P new chocolates if you return N empty chocolate packets. You need to find out the total number
#of chocolates that you can have and print it.
#================================
#Sample Input 1:
#100
#4
#1
#Sample Output 1:
#133
