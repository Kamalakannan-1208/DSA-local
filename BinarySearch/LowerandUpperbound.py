

def lowerbound(arr,s,e,target):
    """To find the element if exist return of first found not then return position where element 
    to be inserted(greater element)"""
    ans=-1

    while(s<=e):
        mid=(s+e)//2
        
        if arr[mid]>=target:
            ans=mid
            e=mid-1
        else:
            s=mid+1
        
    return ans


def upperbound(arr,s,e,target):
    """To find the element if exist return of last found element index not then return position where element 
    to be inserted(greater element)"""
    ans=-1

    while(s<=e):
        mid=(s+e)//2
        
        if arr[mid]>=target:
            ans=mid
            e=mid-1
        else:
            s=mid+1
        
    return ans

arr=[1,2,3,3,7,8,9,9,9,11]
target=4
result=lowerbound(arr,0,len(arr)-1,target)
print(result,arr[result])