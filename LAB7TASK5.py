import numpy as np

vec1 = np.array([1,2,3,7])
vec2 = np.array([4,5,6,9])
temp = 1
total=0
for i in range(vec1.size):
    total+=vec1[i]*vec2[i]
if total%2==0:
    for j in range(vec1.size):
        if j%2==0:
            temp=vec1[j]
            vec1[j]=vec2[j]
            vec2[j]=temp
else:
    for j in range(vec1.size):
        if j%2!=0:
            temp=vec1[j]
            vec1[j]=vec2[j]
            vec2[j]=temp
print(f'Dot Product:{total}')    
print('After Swapping:')
print(vec1,vec2,sep='\n')

#Suppose, you are given two 1D NumPy arrays (vectors). Now, using a loop, find the dot product of these two arrays and print the result.
#  If the result is even, then swap the elements in the even index of the arrays. If the result is odd,
#  then swap the elements in the odd index of the arrays. [You may assume that the size of both the arrays will be the same. 
# Your code should work for 1D arrays of any size. You can not use in-built dot(), sum() or @ to solve this problem.]
#The dot product of two vectors is defined by the summation of element wise multiplication of those two vectors.
#https://docs.google.com/document/d/1z_OwGK6VbMbMmmMEnZxma1umeNardZUYWLnUl_WTjHU/edit
