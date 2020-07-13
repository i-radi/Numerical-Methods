from numpy import *
def absmax(x):
    max=abs(x[0])
    for row in x:
        if abs(row)>max:
            max=abs(row)
    return max
n=int(input("enter number iterations:"))
a=mat(input("enter matrix A:"))
x=[mat(input("enter vector X:"))]
max,l=[0],[0]
for i in range (n):
    x.append(matmul(a,x[i]))
    max.append(absmax(x[i+1]))
    print(f'X{[i+1]}={x[i+1]}')
    print(f'norm {[i+1]}={max[i+1]}')
    if i>0:
        l.append(max[i+1]/max[i])
        print(f'lambda{[i]}={l[i]}')
print(f'\nX{n}={x[n]/max[n]}')