#brutte force map based solution

arr1 = [1,1, 2, 3,5,6,7]
arr2 = [2,3,3,4]

frequency_map = {}

for i in range(len(arr1)):
    frequency_map[arr1[i]] = frequency_map.get(arr1[i],0)+1
for j in range(len(arr2)):
    frequency_map[arr2[j]] =  frequency_map.get(arr2[j],0)+1

result=sorted(frequency_map.keys())

print(result)

#TC : O(n+m)*log(n+m) map add and insertion  and SC : O(n+m) store map and return result O(n+m)


#set based solution
temp=set()

for i in range(len(arr1)):
    temp.add(arr1[i])
for j in range(len(arr2)):  
    temp.add(arr2[j])

result=sorted(temp)
print(result)

#TC : O(n+m)*log(n+m) set add and insertion  and SC : O(n+m) store set and return result O(n+m)


#optimal two pointer solution

i,j=0,0
m=len(arr1)
n=len(arr2)
result=[]

while i<m and j<n:
    result_len=len(result)
    if arr1[i]==arr2[j]:
        if result_len==0 or result[-1]!=arr1[i]:
            result.append(arr1[i])
        i+=1
        j+=1
    elif arr1[i]<arr2[j]:
        if result_len==0 or result[-1]!=arr1[i]:
            result.append(arr1[i])
        i+=1
    else:
        if result_len==0 or result[-1]!=arr2[j]:
            result.append(arr2[j])
        j+=1

while i<m:
    if result_len==0 or result[-1]!=arr1[i]:    
        result.append(arr1[i])
    i+=1
while j<n:
    if result_len==0 or result[-1]!=arr2[j]:
        result.append(arr2[j])  
    j+=1
print(result)

#TC : O(n+m) traverse both arrays and SC : O(n+m) store result