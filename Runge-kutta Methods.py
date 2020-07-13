from math import *
Xo,Yo,h,Xg=float(input("inter Xo")),float(input("inter Yo")),float(input("inter h")),float(input("inter Xgiven"))
n=ceil((Xg-Xo)/h)
x,y,k,l=[Xo],[Yo],[],[]
f=open('d://Runge-kutta method.csv','a')
print('n,Xn,Yn,Kn,Ln,Yn+1',file=f)
for i in range (n+1):
    x.append(x[i]+h)
    k.append(x[i]+y[i]**2)
    l.append(x[i+1]+(y[i]+h*k[i])**2)
    y.append(y[i]+(h/2)*(k[i]+l[i]))
    print(f'{i},{x[i]},{y[i]},{k[i]},{l[i]},{y[i+1]}',file=f)