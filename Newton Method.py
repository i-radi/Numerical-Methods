#Equation =e**x -x-2
from math import *
x=[float(input('enter number of Xo:'))]
f=open('d:\\Newton.csv','a')
print(f'n,Xn\n0,{x[0]}',file=f)
n=0
while(1):
    x.append(x[n]-1+(x[n]+1)/(e**x[n]-1))
    n+=1
    print(f'{n},{x[n]}',file=f)
    if abs(x[n]-x[n-1]) < (10**-6):
        exit()