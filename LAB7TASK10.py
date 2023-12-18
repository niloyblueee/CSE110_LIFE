import numpy as np

def TransposeConverter(arr):
    row=arr.shape[0]
    col=arr.shape[1]
    new=np.zeros(shape=(col,row),dtype=int)
    for i in range(row):
        for j in range(col):
            new[j][i]=arr[i][j]
    print(new)

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[1,2,3,4],
              [1,4,9,16]])


TransposeConverter(A)
TransposeConverter(B)
#https://docs.google.com/document/d/1z_OwGK6VbMbMmmMEnZxma1umeNardZUYWLnUl_WTjHU/edit
#Subtask 10.1: Suppose, you are given a matrix of dimension M×N called A. 
# You have to transpose the matrix in a new 2D array. Finally, print the new array. 
# Your program should work for any given 2D Arrays of size M×N. 
#The transpose of a matrix is a new matrix that is obtained by exchanging the rows and
# columns of the original matrix. Given a matrix A with dimensions M×N, the transpose
#  AT will have dimensions N×M, where the rows of A become the columns of  AT and vice versa.