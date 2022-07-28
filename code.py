import math
sum=0
t=2
def lcmOfNumbers(a,b):
    global t
    res=1
    if t>a or t>b:
        return a*b
    else:
        if a%t==0 and b%t==0:
            a=a//t
            b=b//t
            res=t
        else:
            t+=1
        print(a,b,t)
        return res * lcmOfNumbers(a//t,b//t)
        


test = int(input())
for _ in range(0,test):
    a,b=map(int,input().split())
    t=2
    print(lcmOfNumbers(a,b))
    
