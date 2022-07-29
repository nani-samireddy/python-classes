import math

def gcd(a,b):
    res = 0
    while(a>0 and b>0):
        if(a>b):
            a=a%b
        else:
            b=b%a
    if a>b:
        return a
    else:
        return b


test = int(input())
for _ in range(0,test):
    a,b=map(int,input().split())
    t=2
    print("GCD is=",gcd(a,b))
    
