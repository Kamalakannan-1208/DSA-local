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

