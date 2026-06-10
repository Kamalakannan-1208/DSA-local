arr=[2,1,5,4,3,0,0]
index=-1
def next_permutation(arr):
    for i in range(len(arr)-2, -1, -1):
        if arr[i] < arr[i+1]:
            index=i
            break
    if index==-1:
        arr.reverse()
        return arr
    for j in range(len(arr)-1, index, -1):
        print(arr[j],arr[index])
        print(arr)
        if arr[j] > arr[index]:
            arr[index], arr[j] = arr[j], arr[index]
            break
    arr[index+1:] = reversed(arr[index+1:])
    return arr
    


print(next_permutation(arr))