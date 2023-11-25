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

def calc_yearly_tax():
    age=int(input('Enter age: '))
    total=0
    salarys=[]
    for months in range(1,13):
        salary=int(input('your salary: '))
        salarys.append(salary)
    for salary in salarys:
        tax=calc_tax(age,salary)
        total+=tax
        print(f'month{months} tax: {tax}')
    print('Total Yearly Tax:',total)

calc_yearly_tax()

#yearly tax counter