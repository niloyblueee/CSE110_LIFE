#Home Task 1: Print elements of a 2d array by accessing it column wise first then row wise.
#Ex: if array is [[1, 2, 3],
#                 [4, 5, 6]]
#Output should be: [1 4] 
#                  [2 5]
#                  [3 6]

import numpy as np
primary=np.array([[1, 2, 3],
                 [4, 5, 6]])

for num in range(len(primary[0])):     
    print(primary[0][num],end=' ')                                    
    for num2 in range(num,len(primary[1])):                                 
          print(primary[1][num2],sep=' ')
          break  
          