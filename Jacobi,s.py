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

x1,x2,x3=[0],[0],[0]
c=float(input("enter the tolerance"))
f = open("d:\\Jacobi,s.csv", "w")
print ("m,X1,X2,X3",file=f)
print ("0,0,0,0",file=f)
i=0
while 1:
    x1.append((a[0,3]-(a[0,1]*x2[i]+a[0,2]*x3[i]))/a[0,0])
    x2.append((a[1,3]-(a[1,0]*x1[i]+a[1,2]*x3[i]))/a[1,1])
    x3.append((a[2,3]-(a[2,0]*x1[i]+a[2,1]*x2[i]))/a[2,2])
    i+=1
    print(f'{i},{x1[i]},{x2[i]},{x3[i]}',file=f)
    if abs(x1[i]-x1[i-1])<c and abs(x2[i]-x2[i-1])<c and abs(x3[i]-x3[i-1])<c:
        exit()
