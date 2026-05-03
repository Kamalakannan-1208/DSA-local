# Brutte force approach
no=1234
cnt=0
while(no>0):
    cnt+=1
    no=no//10

print(cnt)

# optimal
import math
n=123
cnt = int(math.log10(n) + 1)
print(cnt)