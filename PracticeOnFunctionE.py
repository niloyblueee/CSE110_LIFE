def BigWordsFinder(x):
    out=x.split()
    inp=[]
    store=0
    for i in out:
        for j in i:
            store+=ord(j)
        if store>700:
            inp.append(i)
            store=0
        else:
            inp=inp
            store=0
    if inp==[]:            
      return 'No big word found'
    else:        
      return inp  

print(BigWordsFinder("Hello World nice to meet you"))

#Write a function BigWordsFinder that takes a string and appends all the words in a list
#  that has a cumulative ascii
#value of more than 700. If there is one or more elements on that list, return it. Otherwise 
# return "No big word found".
#You are allowed to use the .split() function. For your convenience, assume that all the words
#  will only be separated
#by spaces. To calculate the cumulative ascii of each word, add the ascii values of all the 
# characters in that word.