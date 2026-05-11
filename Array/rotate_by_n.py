
# brutte force solution
lst=[1,2,3,4,5,6,7]
d=2
optimize_d=d%len(lst)

temp=[]

# store in temp 
for i in range(optimize_d):
    temp.append(lst[i])

#shift the remaining elements to left
for i in range(optimize_d,len(lst)):
    lst[i-optimize_d]=lst[i]

# copy the temp elements to the end of the list
j=0
for i in range(optimize_d):
    lst[len(lst)-optimize_d+i]=temp[j]
    j+=1

#tc O(n-optimize_d)+O(optimize_d)+O(optimize_ d) => O(n+optimize_d) => O(n)
#sc O(optimize_d) for temp list

print("Left rotated list brute force",optimize_d,":",lst)



#optimal solution

# refer note book tricky optimal split array into two parts and reverse the two parts
# whole array reverse

#function to reverse a list from start to end index 
def reverse_lst(lst,start,end):
    while start<end:
        lst[start],lst[end]=lst[end],lst[start]
        start+=1
        end-=1

lst=[1,2,3,4,5,6,7]
# left rotate by n places 
llst=[3,4,5,1,2]
# right rotate by n places
rlst=[4,5,1,2,3]
by=40
by=by%len(lst)
reverse_lst(lst,0,by-1)
reverse_lst(lst,by,len(lst)-1)
reverse_lst(lst,0,len(lst)-1)
print("Left rotated list by",by,":",lst)    
print("--------------")


reverse_lst(lst,len(lst)-by,len(lst)-1)
print("Reversed part:",lst)

#Tc O(2n) => O(n)
#Sc O(1)
