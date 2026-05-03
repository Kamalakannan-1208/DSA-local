n=10
cpy_n=n
        # code here
reverse=0
while(n>0):
    reverse=(reverse*10)+(n%10)
    n=n//10
print(cpy_n,reverse,cpy_n**reverse)