def show_palindrome(n):
    s=''
    for i in range(1,n):
        s+=str(i)
    for j in range(n,0,-1):
        s+=str(j)
    return s

print(show_palindrome(9))

#print the palindrome of given integer