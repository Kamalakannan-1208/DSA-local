#prb stat: remove a duplicate element from an sorted array inplace return and give unique element count
arr=[1,1,2,2,3,4,4,5]  
index=0

#Approach 1: two pointer approach
#Notes: index pointer will keep track of the last unique element and i pointer will traverse the array to find the next unique element. When a new unique element is found, index is incremented and the new unique element is placed at index position. Finally, index+1 will give the count of unique elements in the array. The array will be modified in place to contain only unique elements up to index position.
#tc: o(n) sc: o(1)
for i in range(1,len(arr)):
    if arr[i]!=arr[index]:
        index+=1
        arr[index]=arr[i]
print(index+1)
print(arr)



#Approach 2 use set method