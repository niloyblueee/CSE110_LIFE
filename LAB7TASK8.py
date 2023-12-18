import numpy as np
def identify(arr):
    count=0
    flag=True
    row=arr.shape[0]
    for i in range(row):
        for j in range(row):
            if arr[i][j]==1 or arr[i][j]==0 :
                count=count
            else:
                count=10
            if arr[i][j]==1:
                count+=1 
    for idx1 in range(row):           
        if arr[idx1][idx1]==1:
            flag=True 
        else:
            flag=False                  
    if count!=arr.shape[0] or flag==False:
        print('Not an Identity Matrix')
    elif count==arr.shape[0] and flag==True:
        print('Identify Matrix') 


a = np.array([ [1, 0, 0],
               [0, 1, 0],
               [0, 0, 1] ])
identify(a)

#You are given a square matrix A of size N×N. Check whether the given matrix is an Identity matrix or not. 
# If it is, then print "Identity matrix" or otherwise print "Not an Identity matrix".
#  Your program should work for any given 2D Arrays of size N×N. 
#[You may need to use the concept of flag and break to solve this problem.]
#Identity Matrix is a square matrix with 1’s along the diagonal from upper left to lower right and 0’s in 
# all other positions. 
##https://docs.google.com/document/d/1z_OwGK6VbMbMmmMEnZxma1umeNardZUYWLnUl_WTjHU/edit
