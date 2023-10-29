s1=input('')
s2=input('')
s3=''
s4=''
for i in range(len(s2)):
 if 'a'<=s2<='z':
   s4+=chr(ord(s2[i])-32)
for index in range(len(s1)):
    if s1[index] in s2 :
      s3=s3
    if s1[index] in s4 :
      s3=s3
    elif s1[index] not in s2 :
      s3+=s1[index] 
       
print(s3)