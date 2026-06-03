arr=[1,0,2,1,0, 2, 1, 2, 0, 1]

#brute force
#use any sorting algorithm eg. merge sort TC O(nlogn) + O(n) and SC O(n)

#better approach
#counting sort TC O(2n) and SC O(1)

count=[0,0,0]
for i in range(len(arr)):
    count[arr[i]]+=1
index=0
for i in range(3):
    for j in range(count[i]):
        arr[index]=i
        index+=1
print(arr)

#optimal approach
#Dutch National Flag Algorithm TC O(n) and SC O(1)  
low=0
mid=0   
high=len(arr)-1
while mid<=high:
    if arr[mid]==0:
        arr[low],arr[mid]=arr[mid],arr[low]
        low+=1
        mid+=1
    elif arr[mid]==1:
        mid+=1
    else:
        arr[mid],arr[high]=arr[high],arr[mid]
        high-=1
print(arr)

