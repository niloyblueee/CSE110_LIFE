s=input('give string: ') #abcd
s2=''
if 'A'<= s <= 'Z':
    print('invalid input')
    
else:
    for index in range(len(s)):
        if ord(s[index])==122:
            s2+='a'
            continue

        s2+=chr(ord(s[index])+1)
print(s2)