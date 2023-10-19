nsmall=int(input('enter year of start: '))
nbig=int(input('enter year of end: '))
for leap_year in range(nsmall,nbig+1,1):
    if leap_year%4==0 and leap_year%100==0 and leap_year%400==0:
        print(leap_year,end=" ")
    elif leap_year%4==0 and leap_year%100!=0:
        print(leap_year,end=" ")
    elif leap_year%400==0:
        print(leap_year,end=" ")        
#task4
#4. Take two-year Inputs from the user (Lower bound and upper bound).
#Print all the years that are leap years within that range (inclusive).
#three conditions are used to identify leap years:
#● The year can be evenly divided by 4, is a leap year, unless
#● The year can be evenly divided by 100, it is NOT a leap year, unless:
#● The year is also evenly divisible by 400. Then it is a leap year.
#[which implies -
#if the year can be divided by 4 and NOT divided by 100, then it’s a leap year.
#If the year can be divided by 4, divided by 100, and divided by 400, then it’s a leap year.]
#https://drive/folders/1yR0Rv_4Owffwht1XiDJMCxRIAZPmEp_P