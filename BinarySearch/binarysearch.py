
def binary_search(arr,target):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=(start+end)//2 #
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return -1


if __name__=="__main__":
    arr=[4,7,10,15,20]
    print(binary_search(arr, 60))