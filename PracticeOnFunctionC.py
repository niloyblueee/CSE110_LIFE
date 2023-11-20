def lower_vowel_extractor(x):
    l=[]
    for i in x:
     if i in 'aeiou':
         if i not in l:
            l.append(i)
    return l


print(lower_vowel_extractor ("CSE110 was not fun. I hope I don’t have to retake."))

#Write a function lower_vowel_extractor that takes a string, extracts all the unique lower-case vowels and appends
#them in a list. Then returns the list. You cannot use .isLower() or .isUpper() built-in functions. One lower-case vowel
#must not occur twice in the returned list.