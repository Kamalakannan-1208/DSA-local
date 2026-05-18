arr=[1,2,2,3,3,4,5,6]
arr1=[2,3,3,5,6,6,7]
len_m=len(arr)
len_n=len(arr1)
#Two pointer solution
i,j=0,0
result=[]
while i<len_m and j< len_n:
    if arr[i]==arr1[j]:
        result.append(arr[i])
        i+=1
        j+=1
    elif arr[i]<arr1[j]:
        i+=1
    else:
        j+=1
        
print(result)


#TC : O(n+m) and SC : O(1)