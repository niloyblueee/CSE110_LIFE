#task3
x=int(input('enter length of side1: '))
y=int(input('enter length of side2: '))
z=int(input('enter length of side3: '))

s=(x+y+z)/2
r1=(s-x)*(s-y)*(s-z)
r2=r1**0.5
r3=s*r2
print(r3)

#Write a python code of a program that reads 
# the values for the three sides x, y, and z of a
#triangle, and then calculates its area.
#  The area is calculated as follows: