import math

def lcm(a,b):
    t=2
    res=1
    while(a>=t and b>=t):
        if(a%t==0 and b%t==0):
            a=a//t
            b=b//t
            res=res*t
        else:
            t+=1        
    return res*a*b

def arrLCM(arr):
    res=arr[0]
    for i in range(1,len(arr)):
        res=lcm(res,arr[i])
    return res
        


n = int(input())
arr = [0]*n
for _ in range(0,n):
    arr[_]=int(input())
print(arrLCM(arr))
    
