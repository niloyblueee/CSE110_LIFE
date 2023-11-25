def show_palindrome(n):
    s=''
    for i in range(1,n):
        s+=str(i)
    for j in range(n,0,-1):
        s+=str(j)
    return s

def show_dots(n):
    return '.'*n

def show_triangle(n):
    for i in range(1,n+1):
        print(show_dots(n-i),end='')
        print(show_palindrome(i),end='')
        print(show_dots(n-i),end='')
        print()
    return    

show_triangle(int(input('')))      


#Write a function called show_triangle that takes a number as an argument and then prints a palindromic triangle.
#Moreover, the empty spaces surrounding the triangle are filled with dots(.) . 
#input 5
#output 
#....1....
#...121...
#..12321..
#.1234321.
#123454321
