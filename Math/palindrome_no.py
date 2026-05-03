temp=1221
no=1221
reverse=0
while no>0:
    
    reverse= (reverse*10)+no%10
    no=no//10

print(temp==reverse)
