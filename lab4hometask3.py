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

#Write a Python program that takes a string
# as an input from the user containing all
#  small letters and then prints the next 
# alphabet in sequence for each alphabet in
#  the input.
#input:abcd
       #the cow
       #xyzabc


#output:bcde
       #uif!dpx
       #yzabcd
