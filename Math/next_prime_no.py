from math import sqrt
def next_prime(n):
    num=n+1
    while True:
            
        is_prime=True
        for i in range(2,int(sqrt(num))+1):
                
            if num%i==0:
                is_prime=False
                break
                
        if is_prime:
            return num
        
        num+=1
n=int(input("Enter a number: "))
print("Next prime number is:",next_prime(n))