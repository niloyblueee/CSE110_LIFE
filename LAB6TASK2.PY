storage=input('')
out=''
n=1
main=storage[1:len(storage)-1] #5, -5, 100, 1, 0
for idx in range(len(main)):
    if main[idx]==',':
        out+=' '
    elif main[idx]==' ':
        out=out
    else:    
        out+=main[idx]
out=out.split()
main2=[]
for j in out:
    main2=[int(j)] + main2
print(main2)

#Take a list of 5 elements as user input and print the list in reverse order. Slicing can be used handling the given list as input. But to reverse the list you must not use slicing and split( ). Hint: You may use a loop to show the reversed list as a new list.
#https://docs.google.com/document/d/14dsdprhPk_wr3AeXdSxKhq2x5Pz0H-rZ/edit