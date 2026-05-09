arr=[1,2,3,4,5]

# brute force with extra space
#optimal approach

pointer=arr[0]
length=len(arr)
for i in range(1,length):
    arr[i-1]=arr[i]
arr[length-1]=pointer
print(arr)