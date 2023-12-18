import numpy as np

def reverseArray(arr):
    n=0
    n1=arr.size-1
    temp=np.zeros(arr.size,dtype=int)
    for i in range(n1,-1,-1):
        n1-=1
        for j in range(n,arr.size):
            temp[j]=arr[i]
            n+=1
            break
    arr=temp
    return arr
     

arr1 = np.array([4, 2, 6, 5])
arr1 = reverseArray(arr1)
print(arr1)

#Write a Python function named reverseArray that takes a NumPy Array as parameter 
# and using loop modifies & returns the reversed array within the given array. 
# That means inside the function you can not create a new array. 
#https://docs.google.com/document/d/1z_OwGK6VbMbMmmMEnZxma1umeNardZUYWLnUl_WTjHU/edit