list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [10, 11, 12, -13, -14, -15,-16]
out=[]
for i in range(len(list1)):
    if list1[i]%2==0:
        out+=[list1[i]]

for j in range(len(list2)):
    if list2[j]%2==0:
        out+=[list2[j]]

print(out)

#Suppose you have two given lists. Write a Python program that creates a new list with all the even elements of both of the given lists and prints the new list. Your program should work for any two given lists
#https://docs.google.com/document/d/14dsdprhPk_wr3AeXdSxKhq2x5Pz0H-rZ/edit