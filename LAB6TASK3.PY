main=input('')
out=''
n=1
counter=0
for idx in range(len(main)):
    if main[idx]==',':
        out+=' '
        counter+=1
    elif main[idx]==' ':
        out=out
    else:    
        out+=main[idx]
out=out.split()
main2=[]
def listing():
    global main2
    for j in out:
        main2+=[int(j)]
    main2=main2[2:len(main2)-2]    
    print(main2)
if counter>2:
    listing()
else:
    print('Not Possible')    


#Write a Python program that takes an input from the user, then prints a new list excluding the first and last two elements of the given list. In case of not enough elements in the list, print "Not possible". Hint: May use list slicing but not split( )
#https://docs.google.com/document/d/14dsdprhPk_wr3AeXdSxKhq2x5Pz0H-rZ/edit    