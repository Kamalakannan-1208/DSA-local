# itsis a looping approach recursion approach also exist and good one
def power(base_value,power_value):
    temp_power_value=power_value
    ans=1
    while(power_value>0):
        if power_value%2==1: # odd
            ans=ans*base_value  
            power_value=power_value-1
        else: 
            power_value=power_value//2
            base_value=base_value*base_value

    if temp_power_value>0: #negative no as power
        ans=1//ans
    return ans

print(power(2,-5)) # it works for -ve no as power

#2^-5 => 1/2^5

