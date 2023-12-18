import numpy as np 

def printPairs(arr,n):
    count=0
    for j in range(len(arr)):
        temp=arr[j]
        for i in range(j+1,len(arr)):
            if arr[i]+temp==n:
                count+=1
                print(temp,arr[i],sep=',')
    if count==0:
        print('No Pair Found')

arr3 = np.array([5, 9, 7, 6, 10])
printPairs(arr3, 18)

#Write a Python function named printPairs that takes an array of numbers
#  and a single integer value as parameters and prints the pairs of two array
#  elements inside the function whose sum is equal to that integer value. 
# If no such pair is found, then print "No Pair Found".
#https://docs.google.com/document/d/1z_OwGK6VbMbMmmMEnZxma1umeNardZUYWLnUl_WTjHU/edit


