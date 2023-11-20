def star_pattern(index):
    if index==0:
        return  
    else:
        if index==4 or index==1:
            print('*'*4)
        else:
            print('*','','*') 
        star_pattern(index-1)       

star_pattern(4)              
