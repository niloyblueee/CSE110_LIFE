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

#Write a python program that takes a string as an input from 
#the user and then modifies the string in such a way that the
#string always starts with an uppercase letter and the case of
#each subsequent letter is the opposite of the previous letter 
#(uppercase character followed by a lowercase character followed
#by an uppercase character and so on). Finally, the modified string
#is printed to show the user
#input:
      #I       love         Python         Programming
      #Python programming is very easy
      #CSE110 Course
#output:
      #I       lOvE        pYtHoN        pRoGrAmMiNg
      #PyThOn PrOgRaMmInG iS vErY eAsY
      #CsE110 cOuRsE
