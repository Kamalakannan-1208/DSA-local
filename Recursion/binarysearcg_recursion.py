"""what are things does in loop might be done using recursion
    TC -> O(logbase2n)
    SC -> O(1)"""

list=[1,2,3,4,5]
target=5
s=0
e=len(list)-1

def binarysearch(arr,s,e,target):

    mid=(s+e)//2

    if s>e:
        return -1
    
    if arr[mid]==target:
        return mid
    
    elif arr[mid]>target:
        return binarysearch(arr,s,mid-1,target)
    
    return binarysearch(arr,mid+1,e,target)
    
result=binarysearch(list,s,e,target)
print(result)