arr=[3,2,10,1]
max=min=arr[-1]
for i in arr:
    if i<min:
        min=i
    elif i>max:
        max=i

print(max,min)
