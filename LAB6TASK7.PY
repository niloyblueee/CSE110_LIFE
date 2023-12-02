def main_linear(given,index=0,output=[]):
    if index==len(given):
        return output
    elif type(given[index])==list:
        main_linear(given[index],0,output)
    else:
        output.append(given[index]) 
    return main_linear(given,index+1,output)
    
def nested_to_linear(res):
  result = main_linear(res)
  print(result)


nested_to_linear(["start", 10, [4, 2, [11, [9, "mid", 3, [1, 0], 6]], 8], "Done"])



#Design a recursive function called nested_to_linear that takes a nested list from the user, and returns the nested list as a linear one. Please refer to the example below to design your program and check with the sample input below.
#Note: Recursion must be used in the nested_to_linear function instead of loop


