arr=[5, 2, 8, 1, 9 ]

f_larg=s_larg=float('-inf')

for i in arr:
    if i>f_larg:
        f_larg,s_larg=i,f_larg
    elif i>s_larg and i<f_larg:
        s_larg=i

print(f_larg,s_larg)