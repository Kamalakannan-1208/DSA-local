#brutte force O(n^3) approach sc O(1)

#better approach is O(n^2) sc O(1)

#optimal approach is O(n) sc O(1) using kadane's algorithm
arr=[-2,1,-3,4,-1,2,1,-5,4]

maxi=float('-inf')
sum=0
for i in arr:
    sum+=i
    if sum>maxi:
        maxi=sum
    if sum<0:
        sum=0
print(maxi)


#follow up question is to print the sub array with maximum sum

maxi=float('-inf')
sum=0
start=0
end=0
for i in range(len(arr)):
    sum+=arr[i]
    if sum>maxi:
        maxi=sum
        end=i
    if sum<0:
        sum=0
        start=i+1
print(start,end)
print(arr[start:end+1])