arr=[1]
k=3
ans=0
for i in range(len(arr)):
    sum=0
    for j in range(i,len(arr)):
        sum+=arr[j]
        if sum==k:
            ans=max(ans,j-i+1)
        elif sum>k:
            break
        
print(ans)

#TC O(n^2)  SC O(1)
#optimal
l=0
r=0
sum=0
ans=0
n=len(arr)
while(r<n):
    if r<n:
        sum+=arr[r]
    while(sum>k and l<=r):
        sum-=arr[l]
        l+=1
    if sum==k:
        ans=max(ans,r-l+1)
    r+=1
    
print(ans)

#TC O(n)  SC O(1)