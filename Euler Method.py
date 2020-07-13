from math import *
Xo,Yo,h,Xg=float(input("inter Xo")),float(input("inter Yo")),float(input("inter h")),float(input("inter Xgiven"))
n=int((Xg-Xo)/h)
x,y=[Xo],[Yo]
f=open('d://Eulers method.csv','a')
print(f'n,Xn,Yn\n0,{Xo},{Yo}',file=f)
for i in range (n):
    y.append(y[i]-h* y[i]**2 /(1+x[i]))
    x.append(x[i]+h)
    print(f'{i+1},{x[i+1]},{y[i+1]}',file=f)