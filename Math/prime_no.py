from math import sqrt
n=29
cnt=0
"""Definition of prime no: if no have two factors -> prime no . 2 more factor -> not prime no
    TC: sqrt n"""

for i in range(1,int(sqrt(n))+1): # return float 

    if n%i==0: # order is very importatnt 1%10 != 10%1

        cnt+=1
        if (n//i)!=i:  
            cnt+=1


if cnt==2:
    print("prime")
else: 
    print("not prime")