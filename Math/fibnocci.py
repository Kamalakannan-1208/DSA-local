n = int(input())

########### Write your code below ###############


def fibnocci(n):
    if n==0 or n==1:
        return n
    else:
        num_1,num_2=0,1
        for _ in range(1,n):
            temp=num_1      #rewrite logic for temp  num_1,num_2=num_2,num_1+num_2
            num_1=num_2
            num_2=temp+num_2

    return num_2
        
fib = fibnocci(n)
########### Write your code above ###############
print(fib)