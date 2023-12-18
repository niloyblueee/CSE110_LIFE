import numpy as np

orginal=np.zeros(int(input('')),dtype=int)
for i in range(orginal.size):
    orginal[i]=int(input(''))
print("orginal array:",orginal)

for j in range(orginal.size):
    min=orginal[j]
    for k in range(j+1,orginal.size):
        if  min>orginal[k]:  
            orginal[j]=orginal[k]
            orginal[k]=min
            break  
print('Sorted Array:',orginal)        