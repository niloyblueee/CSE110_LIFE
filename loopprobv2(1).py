n=int(input(''))
for row in range(n):
    for j in range(1,n):
        print(j,end="")
    for j in range(n,0,-1):
        print(j,end='')
    break
        

#https://drive.google.com/drive/folders/1yR0Rv_4Owffwht1XiDJMCxRIAZPmEp_P
#Read a number (1-9) from the user and print the sequence given in the sample outputs.
#You have to identify the pattern using the sample Inputs and outputs. 
# Assume that the user will not Input any
#invalid number.
#Sample Input 1:
#4
#Output:
#1234321