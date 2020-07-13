#Equation =e**x -x-2
from math import *
x=[int(input('enter number of Xo:')),int(input('enter number of X1:'))]
f=open('d:\\Secant.csv','a')
print(f'n,Xn\n0,{x[0]}\n1,{x[1]}',file=f)
n=1
while(1):
    x.append((x[n-1]*(e**x[n]-x[n]-2)-x[n]*(e**x[n-1]-x[n-1]-2))/((e**x[n]-x[n]-2)-(e**x[n-1]-x[n-1]-2)))
    n+=1
    print(f'{n},{x[n]}',file=f)
    if abs(x[n]-x[n-1]) < (10**-6):
        exit()