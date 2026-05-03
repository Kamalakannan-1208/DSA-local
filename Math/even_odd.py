num=1111111111111111
#m1
if num%2==0:
    print("even")
else:
    print("odd")


#m2
ans="even" if num%2==0 else "odd"
print(ans)


#m3
def iseven(num):
    return not num&1
if iseven(num):
    print("even")
else:
    print("odd")