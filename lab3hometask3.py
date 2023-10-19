n=int(input(''))
divisor=0
divisor1=0
for a in range(1,n+1):
    if n%a==0:
        divisor+=1
  
for b in range(1,n):
    if n%b==0:
        divisor1+=b

if divisor==2:
  print("Prime number")  
elif divisor1==n:
    print('perfect number')
else:
    print(n,'is not a prime or perfect number')         