s=input('')
s2=s.split(",",len(s))
prod=1
for i in range(len(s2)):
    prod*=int(s2[i])

print(s2)
print('Product:',prod)

#Write a python function that takes a string with
#  multiple numbers separated by commas as input 
# from
#the user. Extract the numbers from the string and make a list and print it. Multiply the numbers of the
#list and print the product. [Hint: You can use split()]
#=====================================================
#Sample Input1:
#1,2,3,4,5
#Sample output1:
#['1', '2', '3', '4', '5']
#Product:120