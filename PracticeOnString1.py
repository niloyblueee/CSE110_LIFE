s=input('')
c1=0 #alphabet counter
c2=0 #digit counter
c3=0 #special counter
for index in range(len(s)):
    if 'A'<=s[index]<='Z' or 'a'<=s[index]<='z':
        c1+=1
    elif '0'<=s[index]<='9':
        c2+=1    
    else:
        c3+=1    
print('The number of Alphabets in the string is:',c1)  
print('The number of Digits in the string is :',c2)
print('The number of Special characters in the string is:',c3) 

#Write a Python program to count the total number of alphabets, 
# digits, and special characters in a string.
##Here, space is considered as a special character.
#====================================================
#Sample Input:
#This is CSE110 Course.
#Sample Output:
#The number of Alphabets in the string is: 15
#The number of Digits in the string is : 3
#The number of Special characters in the string is: 4
