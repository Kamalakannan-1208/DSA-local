num="-28524790"
print(num[-1])
print(2222223%10)

# edge case:not working for negative no

print(abs(-1224)%10)

def getLastDigit(a,b):
# code here 
        if b == "0":
            return 1
    
        
        last_a = int(a[-1])
        
        
        cycles = {
            0: [0],
            1: [1],
            2: [2,4,8,6],
            3: [3,9,7,1],
            4: [4,6],
            5: [5],
            6: [6],
            7: [7,9,3,1],
            8: [8,4,2,6],
            9: [9,1]
        }
        
        cycle = cycles[last_a]
        cycle_len = len(cycle)
    
        
        mod = 0
        for digit in b:
            mod = (mod * 10 + int(digit)) % cycle_len
    
        
        index = mod - 1 if mod != 0 else cycle_len - 1
        
        return cycle[index]

print(getLastDigit(3,2))

#using default function
def getLastDigit(a,b):
       a=int(a)
       b=int(b)
       ans= pow(a,b,10)
       return ans%10
