def percantage(value,n):
    value*=(n/100)
    return int(value)
    

def calc_tax(age,salary):
    if age<18 or salary<10000:
        tax=0
    else:
        if 10000<=salary<=20000:
            tax=percantage(salary,7)
        else:
            tax=percantage(salary,14)  
    return tax        

t = calc_tax(49,42000) #(age,salary)
print(t)


#tax counter
