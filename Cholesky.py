from numpy import *
a=mat(input("enter matrix to be solved 3*3\nenter space between each coefficients \nenter semicolon ; between each rows\n"))
print(a)

if a.all()==a.transpose().all():
    print("matrix is symmetric")
else:
    print("matrix is not symmetric")
    exit()
if (a[0,0]>0 and ((a[1,1]*a[2,2]-a[1,2]*a[2,1])>0) and (linalg.det(a)>0)):
    print("matrix is positive definite")
else:
    print("matrix is not positive definite")
    exit()
l=zeros((3,3))

l[0,0]=sqrt(a[0,0])
l[1,0]=a[1,0] / l[0,0]
l[2,0]=a[2,0]/l[0,0]
l[1,1]=sqrt(a[1,1]-l[1,0]**2)
l[2,1]=(a[2,1]-l[1,0]*l[2,0])/l[1,1]
l[2,2]=sqrt(a[2,2]-l[2,0]**2-l[2,1]**2)

print(f'A=LU\nA={a}\nL={l}\nU={l.transpose()}')