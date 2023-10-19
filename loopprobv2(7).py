n=int(input('no of sides: '))
if 1<=n<=2:
    print('a line can be drawn')
elif 3<=n<=4:
    if n==4:
        length=0
        len1=0
        len2=0
        len3=0
        len4=0
        for sides in range(0,4):
            n2=float(input('length of rectangle: '))
            if sides==0:
                len1=length+n2
            elif sides==1:
                len2=length+n2
            elif sides==2:
                len3=length+n2
            elif sides==3:
                len4=length+n2   
        if (len1+len2+len3>len4 and 
        len1+len2+len4>len3 and
        len1+len3+len4>len2 and
        len3+len2+len4>len1):
            print("A triangle can be drawn") 
        else:
            print('A tritangle cannot be drawn')                     


    elif n==3:
        leng=0
        leng1=0
        leng2=0
        leng3=0
        for sides2 in range(0,3):
            n3=float(input('length of triangle: '))
            if sides2==0:
                leng1=leng+n3
            elif sides2==1:
                leng2=leng+n3
            elif sides2==2:
                leng3=leng+n3
        if (leng1+leng2>leng3 and
            leng3+leng2>leng1 and
              leng1+leng3>leng2):
            print("A rectangle can be drawn") 
        else:
            print('A tritangle cannot be drawn')        
                     
else:
    print('invalid input')

#Imagine you are trying to draw a shape. So, you are taking the lengths of each of the sides of the shape.
#Now, what shape you need to draw depends on the first Input (1-4).
#a.If no of sides: 1 or 2, a line needs to be drawn
#b.If no of sides: 3, a triangle needs to be drawn
#c. If no of sides: 4, a rectangle needs to be drawnQ#d.For any other number of sides, print “Invalid Input”
#After deciding what your shape will be, your job is to verify whether the shape can be drawn using the lengths
#given by the user.
#● To draw a triangle, the sum of the lengths of any two sides must be greater than the third.
#● To draw a rectangle, the sum of the lengths of any three sides must be greater than the fourth.
#● To draw a line, no verification is required.
#https://drive.google.com/drive/folders/1yR0Rv_4Owffwht1XiDJMCxRIAZPmEp_P
#task7