arr=[1, 22, 3, 12, 5]
ans=[]
maxi=float('-inf')
for i in range(len(arr)-1, -1, -1):
    
    if arr[i]>maxi:
        ans.append(arr[i])
        maxi=arr[i]
print(ans)

#TC: O(n) and SC: O(n)