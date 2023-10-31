s='I love python programming'
  
s2=''
if 'a'<=s[0]<='z':
        s2+=chr(ord(s[0])-32)
        
elif 'A'<=s[0]<='Z':
        s2+=chr(ord(s[0]))
        
for i in range(1,len(s)):
   
    if s[i-1]==' ':
        if 'a'<=s[i]<='z':
            s2+=chr(ord(s[i])-32)
            continue
        if 'A'<=s[i]<='Z':
            s2+=chr(ord(s[i]))
            continue  
    else:
        s2+=s[i]        
print(s2)



#Write a Python program to Capitalize the 
# first character of each word in a String 
# [You cannot use the
#built-in upper() function]
#Sample Input:
#I love python programming
#Sample Output:
#I Love Python Programming
        
