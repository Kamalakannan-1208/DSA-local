#Note: with return statement
def factorial(n):
    if n == 0:
        return 
    
    print(n,end=" ")
    return factorial(n - 1)
    
factorial(5)