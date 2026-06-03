# majority element greater than n/2 times

arr=[2,2,1,1,1,2]

for i in range(len(arr)):
    count=0
    for j in range(len(arr)):
        if arr[i]==arr[j]:
            count+=1
    if count>len(arr)/2:
        print(arr[i])
        break
#TC -> O(n^2) SC -> O(1)

#Better approach using hash map

mpp={}
for i in arr:
    if i in mpp:
        mpp[i]+=1
    else:
        mpp[i]=1
for key in mpp:
    if mpp[key]>len(arr)/2:
        print(key)
        break
#TC -> O(n) SC -> O(n)

#optimal approach using moore voting algorithm

count=0
element=-1
for i in arr:
    if count==0:
        element=i
    if i==element:
        count+=1
    else:
        count-=1

cnt=0
for i in arr:
    if i==element:
        cnt+=1
if cnt>len(arr)/2:
    print(element)
else:
    print("No majority element")