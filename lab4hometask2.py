s1=input('Give string: ')
s2=''
n1=0 #' '
n2=0 #','
n3=0
s3=''
s4=''
for index in range(len(s1)):
    if s1[index]==',':
        n2=index
    elif s1[index]==' ':
        n1=index
        n3+=n1+1
        break
s3+=s1[0:n2]
s4+=s1[n1+1:]        
if len(s3)>len(s4):
   for index in range(n2):
      s2+=s1[index]
      for j in range(n3,len(s1)):
         s2+=s1[j]
         n3+=1
         break                 
else:                               
    for index in range(n2):
      s2+=s1[index]
      for j in range(n3,len(s1)):
           s2+=s1[j]
           n3+=1
           break
s2+=s1[n1+len(s3)+1:]            
print(s2)
#Write a Python program that will take one input from the user
#made up of two strings separated by a comma and a space (see samples below).
#Then create a mixed string with alternative characters from 
# each string. Any leftover chars will be appended at the end
#  of the resulting string. [Do not use lists for this task]          
#input: ABCD, efgh
#output: AeBfCgDh





