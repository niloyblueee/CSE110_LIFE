import  numpy as np 

orginal=np.zeros(int(input()),dtype=int)
resize=np.zeros(orginal.size+1,dtype=int)
for i in range(orginal.size):
    orginal[i]=int(input())
    resize[i]=orginal[i]
resize[-1]=int(input())
print(f'Orginal Array:{orginal}')
print(f'Resized array:{resize}')   

#Take an integer N as an input from the user and create an 1D array with size N by taking each integer element as user input. Then, print the array. Next, take another integer input from the user. Resize the array and add the new integer value in the new array. Lastly, print the new array. 
# https://docs.google.com/document/d/1z_OwGK6VbMbMmmMEnZxma1umeNardZUYWLnUl_WTjHU/edit
