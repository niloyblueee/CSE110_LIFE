n=int(input(''))
res=0
res2=0
s=''         
for i in range(n):
    res=res*10+1
    res2+=res
    s+=str(res)
    if i!=n-1:
     s+='+'
 
print(s)  
print("the sum is :",res2)  
#Write a Python program that reads a number and finds the sum of the series of 1 +11 + 111 + 1111 +
#....+N terms.
#=====================================================
#Sample Input1:
#5
#Sample Output1:
#1 + 11 + 111 + 1111 + 11111
#The Sum is: 12345