n=int(input(""))
sum=0
for num in range(1,n+1):
    if num%7==0 and num%9!=0:
        sum+=num 
    elif num%9==0 and num%7!=0:
        sum+=num
      
print(sum)  

#https://docs.google.com/document/d/1G5BGPpC3BWBuIO5YzaML-xssgctensS_/edit