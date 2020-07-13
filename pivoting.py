#Patial pivoting Method '3 Equations'
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
#sort descending
if (abs(a[2,0])>abs(a[1,0])) and (abs(a[2,0])>abs(a[0,0])):
    for i in range (4):
        a[2,i],a[0,i]=a[0,i],a[2,i]
if (abs(a[1,0])>abs(a[0,0])):
    for i in range (4):
        a[1,i],a[0,i]=a[0,i],a[1,i]
if (abs(a[2,0])>abs(a[1,0])):
    for i in range (4):
        a[2,i],a[1,i]=a[1,i],a[2,i]

m1=a[1,0]/a[0,0]
m2=a[2,0]/a[0,0]
for j in range(4):
    a[1,j]=a[1,j]-m1*a[0,j]
    a[2, j] = a[2, j] - m2 * a[0, j]
#sort descending
if (abs(a[2,1])>abs(a[1,1])):
    for l in range (4):
        a[2,l],a[1,l]=a[1,l],a[2,l]

m3=a[2,1]/a[1,1]
for k in range (1,4):
    a[2, k] = a[2, k] - m3 * a[1, k]

z=a[2,3]/a[2,2]
y=(a[1,3]-a[1,2]*z)/a[1,1]
x=(a[0,3]-a[0,2]*z-a[0,1]*y)/a[0,0]
print(f'x={round(x,4)},y={round(y,4)},z={round(z,4)}')