# edge case negative no , after rev no must be include within 2 31 to - 2 32-1 
# TC divide no so log(n)
# SC O(1)

given_no = 2147483647
rev_no=0

# check sign 
if given_no <0:
    sign=-1
    given_no=given_no*sign
    print(given_no)
else:
    sign=1


while given_no:
    last_digit= given_no%10
    print("last digit",last_digit)
    rev_no= rev_no*10+last_digit
    given_no=given_no//10


if rev_no >= 2 ** 31 - 1 or rev_no <= -(2 ** 31): # reversed no bit is within or not
    rev_no=0
