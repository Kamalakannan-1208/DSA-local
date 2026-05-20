arr=[1,2,3,5]
n=5

# Method 1 Linear search
for i in range(1,n+1):
    found=False
    for j in arr:
        if j==i:
            found=True
            break
    if not found:
        print(i)

# Method 2 using sum formula
total_sum=n*(n+1)//2
arr_sum=sum(arr)
missing_no=total_sum-arr_sum
print(missing_no)

# Method 3 using xor
sum=0


for j in range(n-1):
    sum^= (1+j)
    sum^=arr[j]
sum^=n
print(sum)

#Tc: O(n) SC: O(1)

#eg: sum=1^1^2^2^3^3^4^5^5
