def reverse_lst(lst,start,end):
    while start<end:
        lst[start],lst[end]=lst[end],lst[start]
        start+=1
        end-=1

lst=[1,2,3,4,5]
reverse_lst(lst,0,len(lst)-1)
print("Reversed list:",lst)