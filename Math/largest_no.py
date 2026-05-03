list=[1,2,3,4,5]
print(max(list))

import sys
value=-sys.maxsize # for minimum value
# sys.maxsize for max value
print(value)
print(type(value))
for i in list:
    if i>value:
        value=i

print(value)