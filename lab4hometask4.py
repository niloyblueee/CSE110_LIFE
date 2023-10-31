s=input('')
s1=''
counter=0
for char in s:
  if 'a'<=char<='z' or 'A'<=char<='Z':
     if counter%2==0:
        if 'a'<=char<='z' :
           print(chr(ord(char)-32),end='')
        elif 'A'<=char<='Z':
           print(chr(ord(char)),end='')
     else:
       if 'A'<=char<='Z':
         print(chr(ord(char)+32),end='')
       elif 'a'<=char<='z':
         print(chr(ord(char)),end='')
     counter+=1    
  else:
    print(char,end='') 
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
