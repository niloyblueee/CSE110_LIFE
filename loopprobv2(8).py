n=int(input('no of angles: '))
angles=0
if n==3:
    for i in range(n):
        n2=int(input('angles: '))
        angles+=n2
    if angles==180:
         print('A triangle can be drawn')
    else:
         print('Triangle cannot be drawn')
        
elif n==4:    
    for i in range(n):
       n2=int(input('angles: '))
       angles+=n2
    if angles==360:
        print('A rectangle can be drawn')
    else:
        print('Rectangle cannot be drawn')    
else:
    print('Invalid number of angles')    

#8. Imagine you are trying to draw a shape. So, you are taking the angles of the shape. Now, what shape you need
#to draw depends on the first Input (3 or 4).
#a.If no of angles is 3, a triangle needs to be drawn
#b.If no of angles is 4, a rectangle needs to be drawn
#c. For any other Inputs, print “Invalid Input”
#After deciding what your shape will be, your job is to verify whether the shape can be drawn using the angles given
#by the user.
#● To draw a triangle, the sum of the angles must be equal to 180 degrees.
#● To draw a rectangle, the sum of the angles must be equal to 360 degrees.    


