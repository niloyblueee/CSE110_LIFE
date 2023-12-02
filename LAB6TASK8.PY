out=[]
for intakes in range(5):
    storage=[]
    inp=input()
    main=inp[1:len(inp)-1]
    for i in range(len(main)):
        temp=''
        if main[i]==',':
            temp+=main[:i]
            storage.append(temp)
            temp=''
            temp+=main[i+1:]
            storage.append(float(temp))           
            out.append(storage)
            print(out)
            break


#Assume you have a class of five students. And as a faculty you need to
#  enter their name and CSE110 GPA in a list called grade_list. This particular
#  grade_list consists of individual lists of the student's name and GPA. Hence,
#  it makes the grade_list a nested list / list of lists.
#Particular student information will be given as input by the faculty. Please refer 
# to the example below to design your program.

#https://docs.google.com/document/d/14dsdprhPk_wr3AeXdSxKhq2x5Pz0H-rZ/edit

    













