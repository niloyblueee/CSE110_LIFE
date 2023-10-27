s=input('Give string: ')
s2=s
s1=''
for index in range(len(s)):
    if s[index]==s2[index-1]:
        s1=s1
    elif s[index]==s2[index]:
        s1+=s[index]        
print(s1)   