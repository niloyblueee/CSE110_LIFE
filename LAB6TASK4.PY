List_one = [1, 4, 3, 2, 5]
List_two = [8, 7, 6, 9]
flag=True
for i in List_one:
    for j in List_two:
        if i==j:
            flag=True
            break
        else:
            flag=False

print(flag)  

#Let’s assume, you have two given lists: List_one and List_two. Write a Python program that prints "True", if the given two lists have at least one common member. Otherwise, prints "False".
#Hint: Please use concepts of flag and break to solve this task.
#https://docs.google.com/document/d/14dsdprhPk_wr3AeXdSxKhq2x5Pz0H-rZ/edit
            
