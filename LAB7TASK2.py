import  numpy as np 

orginal=np.zeros(int(input()),dtype=int)
modi=np.zeros(orginal.size,dtype=int)
for i in range(orginal.size):
    n=int(input())
    orginal[i]=n
    if 0<n:
        modi[i]=1
    elif 0>n:
        modi[i]=0
    else:
        modi[i]=n

print(f'Orginal Array:{orginal}')
print(f'After modifying:{modi}')

#Take an integer N input from the user and create a 1D integer array of N numbers. 
# Then, print the array. Next, modify the array by changing the positive numbers by 1 and the negative numbers by 0.
#  If the element is zero, then it will be unchanged. Lastly, print the modified array.
#https://docs.google.com/document/d/1z_OwGK6VbMbMmmMEnZxma1umeNardZUYWLnUl_WTjHU/edit