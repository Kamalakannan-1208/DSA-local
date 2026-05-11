# prb : move the zeroes to the end of the array 

arr=[0,1,0,3,12]

#Approach 1: brute force with extra space

temp=[]
for i in arr:
    if i!=0:
        temp.append(i)
index=0
for i in range(len(arr)):
    if index<len(temp):
        arr[i]=temp[index]
        index+=1
    else:
        arr[i]=0

print("brutte force",arr)

#TC-> O(temp_size)+O(n) => O(n)
#SC-> O(temp_size) => O(n)


#Approach 2: optimal approach with two pointer approach
#found first zero element
j=-1
for i in range(len(arr)):
    if arr[i]==0:
        j=i
        break
if j==-1:
    print(arr)
else:

    for k in range(j+1,len(arr)):
        if arr[k]!=0:
            arr[j],arr[k]=arr[k],arr[j]
            j+=1
    print("two pointer approach",arr)
    

#TC-> O(j)+O(n-j) => O(n)
#SC-> O(1)
