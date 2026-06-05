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
