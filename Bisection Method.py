#Equation =x**6 -x-1
from math import *
a,b,c,f=[0],[0],[0],[0]
a.append(int(input('enter number of a:')))
b.append(int(input('enter number of b:')))
error=float(input('enter number of error:'))
n=ceil(1/log(2)*log((b[1]-a[1])/error))
fi=open('d:\\bisection .csv','a')
print('n,a,b,c,f(c)',file=fi)
for i in range (1,n+1):
    c.append((a[i]+b[i])/2)
    f.append(c[i]**6-c[i]-1)
    if f[i]==0:
        exit()
    if (a[i]**6-a[i]-1)*f[i] <0:
        a.append(a[i])
        b.append(c[i])
    else:
        a.append(c[i])
        b.append(b[i])
    print(f'{i},{a[i]},{b[i]},{c[i]},{f[i]}',file=fi)