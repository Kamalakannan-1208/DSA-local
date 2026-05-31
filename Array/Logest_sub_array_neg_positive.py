arr=[1,-1,0,1,-1,1,0,1]
k=1
mpp={}
ans=0 
sum=0
for i in range(len(arr)):
    sum+=arr[i]
    if sum==k:
        ans=max(ans,i+1)
    if sum-k in mpp:
        ans=max(ans,i-mpp[sum-k])
    if sum not in mpp:
        mpp[sum]=i
print(ans)
