# if a year is divisible by 4 and not centure year means not divisible by 100, it is a leap year 
# but if the year is divisible by 100 and by 400, then it is a leap year (century year)

year=int(input())

if year%4 ==0 and year%100 !=0:
    print("True") # leap year
    
elif year%100==0  and year %400 ==0:
    print("True") #leap year
    
else:
    print("False") # not a leap year