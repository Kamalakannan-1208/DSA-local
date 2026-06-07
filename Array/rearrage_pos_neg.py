#pattern-1 equal no of positive and negative
#output postive first then negative

arr=[-1,-3,2,4,-5,6]
pos=[]
neg=[]
for i in arr:
    if i>0:
        pos.append(i)
    else:
        neg.append(i)
for i in range(min(len(pos),len(neg))):
    arr[i*2+1]=neg[i]
    arr[i*2]=pos[i]
print(arr)

#Tc O(2n) sc O(n) for extra space

#optimal approach
ans_arr=[0]*len(arr)
pos=0
neg=1
for i in arr:
    if i>0:
        ans_arr[pos]=i
        pos+=2
    else:
        ans_arr[neg]=i
        neg+=2

print(ans_arr)

#Tc O(n) sc O(n) for extra space


##folloup question differenet no of positive and negative size
arr=[-1,-3,-4-5,6]
pos=[]
neg=[]
for i in arr:
    if i>0:
        pos.append(i)
    else:
        neg.append(i)

for i in range(min(len(pos),len(neg))):
    arr[i*2]=pos[i]
    arr[i*2+1]=neg[i]


if len(pos)>len(neg):
    for i in range(len(neg)*2,len(arr)):
        arr[i]=pos[i//2]
else:
    for i in range(len(pos)*2,len(arr)):
        arr[i]=neg[i//2]
print(arr)
