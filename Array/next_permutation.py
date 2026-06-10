#brute force
from itertools import permutations
arr=[2,1,5,4,3,0,0]
def next_permutation_brute_force(arr):
    perms =sorted(set(permutations(arr)))
    current = tuple(arr)
    for i in range(len(perms)):
        if perms[i] == current:
            if i == len(perms) - 1:
                return list(perms[0])
            else:
                return list(perms[i+1])
    return arr

print(next_permutation_brute_force(arr))
#TC: O(n*n!) and SC: O(n*n!)
#optimal
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
        if arr[j] > arr[index]:
            arr[index], arr[j] = arr[j], arr[index]
            break
    arr[index+1:] = reversed(arr[index+1:])
    return arr

#TC: O(n) and SC: O(1)
    


print(next_permutation(arr))