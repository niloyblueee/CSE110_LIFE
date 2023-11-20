def list_to_string(x):
    s=''
    for i in x:
        if i!=',':
            s+=str(i)
    return s



print(list_to_string([-5, 0.3, "3"]))

#Write a function list_to_string that
# takes a list as a parameter, concat all 
# the elements of the list into a string, 
# and returns that string.