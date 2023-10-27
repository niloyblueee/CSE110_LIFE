s1=input('Give string: ')
s2=''
n1=0 #' '
n2=0 #','
n3=0
for index in range(len(s1)):
    if s1[index]==',':
        n2=index
    elif s1[index]==' ':
        n1=index
        n3+=n1+1
        break
for index in range(n2):
    s2+=s1[index]
    for j in range(n3,len(s1)):
        s2+=s1[j]
        n3+=1
        break
        
                   
#s2+=s1[0:n2]+s1[n1+1::]  
print(s2,sep='')            





