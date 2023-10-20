n=input('')
n2=int(n)
res=0
for num in range(len(n),0,-1):
    res2=n2//(10**(num-1))
    n2=n2%(10**(num-1))    
    if num==1:
        print(res2,end='')
    else:
        print(res2,end=',')    
print()

#https://docs.google.com/document/d/1G5BGPpC3BWBuIO5YzaML-xssgctensS_/edit
