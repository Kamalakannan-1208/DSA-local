def third_largest_no(arr):
    first=second=third=-1
    for i in arr:
        # skip duplicate if i in (first,second,third) then continue
        if i>first:
            first,second,third=i,first,second
        elif i>second:
            second,third=i,second
        elif i>third:
            third=i
    return third

print(third_largest_no([1,2,2,3,4,5]))
print(third_largest_no([1,10]))
print(third_largest_no([30,1000,100,432,-4431]))

#TC->O(n) and SC O(1)
