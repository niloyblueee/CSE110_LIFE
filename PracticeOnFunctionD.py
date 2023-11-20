#["I","love","Programming","in","Python"]
def more_than_avg(x):
    n1=0
    n=0
    out=[]
    for i in x:
        if i !=',':
          n1+=1 
        for j in i:
           n+=len(j)
    avg=n/n1
    for i in x:
       if len(i)>avg:
          out.append(i)
    if out==[]:
       return 'No big word found'     
    else:
        return avg,out
       
print(more_than_avg(["CSE110's","Final","Examination","is","extremely","easy"]))

#Write a function called more_than_avg which
#  takes a list of strings as a parameter and 
# returns the average length of
#the strings and a list of strings which are 
#longer than the average length. Finally, print
#the returned result in the
#function call. No need to take user inputs.