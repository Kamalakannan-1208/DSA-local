arr= [2, 7, 11, 15]

#brute force
target =9

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print(i,j) 
            print("yes")

#better approach

map={}
for i in range(len(arr)):
    if target-arr[i] in map:
        print(map[target-arr[i]],i)
    else:
        map[arr[i]]=i
# optimal approach
trace_index=[]
for i in range(len(arr)):
    trace_index.append((arr[i],i))
trace_index.sort()
l=0
r=len(arr)-1
while l<r:
    sum=trace_index[l][0]+trace_index[r][0]
    if sum==target: 
        print(trace_index[l][1],trace_index[r][1])
        break
    elif sum<target:
        l+=1
    else:
        r-=1

