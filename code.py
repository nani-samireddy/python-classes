import math

def gcd(a,b):
    if(a<=0):
        return b
    elif b<=0:
        return a
    if a>b:
        return gcd(a%b,b)
    else:
        return gcd(a,b%a)
        


test = int(input())
for _ in range(0,test):
    a,b=map(int,input().split())
    t=2
    print("GCD is=",gcd(a,b))
    
