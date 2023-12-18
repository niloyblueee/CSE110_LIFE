import numpy as np
def TransposeConverter(arr):
    row=arr.shape[0]
    col=arr.shape[1]
    new=np.zeros(shape=(col,row),dtype=int)
    for i in range(row):
        for j in range(col):
            new[j][i]=arr[i][j]
    return new

a = np.array([[1,2,3,4],
             [1,4,9,16]])
a1=TransposeConverter(a)
n=0
n1=0
out=np.zeros(shape=(a1.shape[0],a.shape[1]),dtype=int)
for k in range(a.shape[1]):
    for i in range(a1.shape[0]):
        for j in range(a1.shape[1]):
            out[n][n1]+=a1[k][j]*a[j][i]
        n1+=1
    n1=0
    n+=1                 
print(out)            
#Using the result from Subtask 10.1, calculate the gram matrix for A. You have to use loops to solve this task.
#When a matrix (A) is multiplied by its transpose (AT), the resulting symmetric matrix (AT×A) 
# is referred to as a "Gram matrix"
#https://docs.google.com/document/d/1z_OwGK6VbMbMmmMEnZxma1umeNardZUYWLnUl_WTjHU/edit