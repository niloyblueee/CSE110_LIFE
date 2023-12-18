import numpy as np
def longconversion(arr):
    res=str(arr.shape[0]-arr.shape[1])
    if res[0]=='-':
        res=int(res[1:])
    else:
        res=int(res)
    remainder=res%arr.shape[0]
    sum=0
    for i in range(len(arr[0])):
        sum+=arr[remainder][i]
    avg=str(sum/len(arr[remainder]))
    n=0
    for idx in range(len(avg)):
        if avg[idx]=='.':
           n=idx
        break  
    new=np.zeros(shape=(arr.shape[0],arr.shape[1]),dtype=float)
    avg=float(avg[:n+4]) 
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            new[i][j]=arr[i][j]*avg
    print(new)        


a = np.array([[6,3], 
            [1,5]])
longconversion(a)
#Suppose, you are given an M×N array called A. Your task is to subtract the row and column numbers and find the absolute difference.
#  Next, find the remainder (rounded to 2 decimal places) by dividing the absolute value by M. Now, 
#If remainder = 0, then find the average of the 1st row. 
#If remainder = 1, then find the average of the 2nd row. 
#If remainder = 2, then find the average of the 3rd row. 
#Similarly, if remainder = m-1, then find the average of the mth row. 
#Now multiply each element of the original array with the average to find out the final array.
#  Finally, display the new array.

#https://docs.google.com/document/d/1z_OwGK6VbMbMmmMEnZxma1umeNardZUYWLnUl_WTjHU/edit