
# Two Pointer Technique
"""Tc -> O(n)
   Sc -> O(1) """
arr=[1,1,2,2,3,4,4,5,5]


def find_unique_element(arr):
    pointer=0
    for i in range(0,len(arr)):
        if arr[i]!=arr[pointer]:
            pointer+=1
            arr[pointer]=arr[i]
    return pointer+1

result=find_unique_element(arr)
print("Number of unique elements:",result)
print("Unique elements are:",arr[:])