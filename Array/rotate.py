"""Tc -> O(n)
   Sc -> O(1) """
arr=[1,1,2,2,3,4,4,5,5]

def left_rotate_array(arr):
    temp=arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[-1]=temp
    
left_rotate_array(arr) # inplace rotation array refer by object  
print("Original array:",arr)

def right_rotate_array(arr):
    temp=arr[len(arr)-1]
    for i in range(len(arr)-2,-1,-1):
        arr[i+1]=arr[i]
    arr[0]=temp
right_rotate_array(arr)
print("Original array after right rotation:",arr)
    