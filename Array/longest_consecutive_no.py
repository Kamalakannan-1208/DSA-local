arr=[1,12,2,3,4,23,13]

#better approach
last_min=float('-inf')
longest=1
cnt=0
sort=sorted(arr)
for i in sort:
    
    if i-1 == last_min:
        cnt+=1
        last_min=i
    if i!= last_min:
        cnt=1
        last_min=i
    longest=max(longest,cnt)
print(longest)

# TC: O(nlogn) due to sorting SC: O(1)
#optimal approach
set_arr=set(arr)
longest_len=1
for i in set_arr:
    if i-1 not in set_arr:
        cnt=1
        while i+1 in set_arr:
            cnt+=1
            i+=1
        longest_len=max(longest_len,cnt)
print(longest_len)
# TC: O(n) SC: O(n) due to set