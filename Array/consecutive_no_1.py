arr=[1,1,0,1,1,1,0,1]

count=0
max=0
for i in range(len(arr)-1):
    if arr[i]==1:
        count+=1
    else:
        if max<count:
            max=count
        count=0
print(max)    