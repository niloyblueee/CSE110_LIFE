#Take a string input from the user and
#check if ‘H’ and ‘e’ are in the string.
#If both characters are there, print,
#‘Both H and e’. Else if, only ‘H’ is in the string,
#print, ‘Only H’. Else if, only ‘e’ is in the string,
#print, ‘Only e’. Else, print, ‘No H or e’

var1=input('')
if 'H' in var1 and 'e' in var1:
    print ('Both H and e')         #task2
elif 'H' in var1:
    print ('Only H')
elif 'e' in var1:
    print ('only e')
else:
    print('No H or e')
