import numpy as np

def AbsoluteDiff(arr):
    row=arr.shape[0]
    prod1=0
    prod2=0
    n=0
    for i in range(row):
        prod1+=arr[i][i]
    for j in range(row-1,-1,-1):
        prod2+=arr[n][j] 
        n+=1
    res=str(prod1-prod2)
    if res[0]=='-':
        res=res[1:]
    else:
        res=res    
    print(res)       


a = np.array([  [1,  5,  12,  1],
                [2,  -4,  6,  7],
                [3,  8,  5,  9],
                [3,  5,  23,  -6] ])
AbsoluteDiff(a)

#You are given a 2D array A of size N×N. Print the absolute difference between the summation
#  of its two diagonals (primary and secondary diagonal). Your program should work for any given 
# 2D Arrays of size N×N. 
#You can use abs() function to calculate the absolute difference.
#https://docs.google.com/document/d/1z_OwGK6VbMbMmmMEnZxma1umeNardZUYWLnUl_WTjHU/edit