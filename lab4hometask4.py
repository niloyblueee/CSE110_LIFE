s=input('give string: ')
s2=''
for index in range(len(s)):
    if index%2==0 and ord('a')<=ord(s[index])<=ord('z'):
        s2+=chr(ord(s[index])-32)
    elif index%2==0 :
        s2+=chr(ord(s[index]))

    elif index%2!=0 and ord('A')<=ord(s[index])<=ord('Z'):
        s2+=chr(ord(s[index])+32)   
    else:
        s2+=chr(ord(s[index]))     
print(s2)        
