import numpy as np

def flatten(arr):
    n=0
    main=np.zeros(arr.size,dtype=int)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            main[n]=arr[i][j]
            n=n+1
    return main


arr1=np.array( [ [1, 2, 3], 
                [3, 4, 5] ] )
arr2 = flatten(arr1)
print(arr2)

arr3 = np.array( [ [1, 4], 
                             [5, 6],
                             [8, 9] ] )
arr4 = flatten(arr3)
print(arr4)

#Write a Python function called flatten that takes a 2D array as parameter and returns an 1D array by 
# flattening the 2D array.
#https://docs.google.com/document/d/1z_OwGK6VbMbMmmMEnZxma1umeNardZUYWLnUl_WTjHU/edit
   