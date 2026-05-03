#Note: without return statement

def n_num(n):
    if n == 0:
        return 
    
    
    n_num(n - 1)
    print(n,end=" ")

n_num(5)