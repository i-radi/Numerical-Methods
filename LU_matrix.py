#LU Decomposition Method '3 Equations'
from numpy import *
def equationStringToDict(eq):
    ret,num,afterDecimalPoint,decimalPlaces,negative,name={},0,False,0,False,''
    for c in eq:
        if c in "!@#$%^&*()_[]{}'/\\,":
            raise Exception(f"Character [{c}] not allowed")
        elif c.isdigit():
            if afterDecimalPoint:
                num+= float('.'+'0'*decimalPlaces+c)
                decimalPlaces +=1
            else:
               num= num*10 + int(c)
        elif c.isalpha():
            name+=c
        elif c=='.':
            afterDecimalPoint= True
        elif c=='+' or c=='=' or c=='-' :
            if name=='' and num ==0:
                negative = c=='-'
                continue
            ret[name]=num*(-1 if negative else 1)
            num,afterDecimalPoint,decimalPlaces,name,negative=0,False,0,'',c=='-'
    ret['Result']=num*(-1 if negative else 1)
    return ret

def fromDictToMatrix(args):
    keys=[]
    for arg in args:
        if 'Result' not in arg.keys():
            raise Exception("No Result Value in Dict")
        for k in arg.keys():
            if k not in keys and k !="Result":
                keys.append(k)
    return [[(arg[k] if k in arg.keys() else 0) for k in keys]+[arg['Result']] for arg in args]

Input= []
for i in range (3):
    Input.append(input(f'enter equation {i+1}'))
x = [equationStringToDict(n) for n in Input]
a=array(fromDictToMatrix(x))
c=a[:,3]

l=identity(3)
u=zeros((3,3))

for j in range (3):
    u[0,j]=a[0,j]
for i in range (1,3):
    l[i,0]=a[i,0]/u[0,0]
u[1,1]=a[1,1]-l[1,0]*u[0,1]
u[1,2]=a[1,2]-l[1,0]*u[0,2]
l[2,1]=(a[2,1]-l[2,0]*u[0,1])/u[1,1]
u[2,2]=a[2,2]-l[2,0]*u[0,2]-l[2,1]*u[1,2]

c[1]-=l[1,0]*c[0]
c[2]-=(l[2,0]*c[0]+l[2,1]*c[1])
x3=c[2]/u[2,2]
x2=(c[1]-u[1,2]*x3)/u[1,1]
x1=(c[0]-u[0,1]*x2-u[0,2]*x3)/u[0,0]
print(f' x1={x1} \n x2={x2} \n x3={x3}')