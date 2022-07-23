
import math as M

def isPrime(n):
    if(n==1):
        return False
    else:
        isprime = True
        end = int(M.sqrt(n))+1
        for i in range(2,end):
            if(n%i==0):
                isprime=False
                break
        return isprime

    
def isSPrime(number):
    primeCounter = 2
    res=False
    counter = int(M.sqrt(number))
    for i in range(2,counter+1):
        if number%i==0 and isPrime(i) and isPrime(number//i):
            res=True
            break
    return res
    
        
    
t = int(input())
for _ in range(0,t):
    num = int(input())
    print(isSPrime(num))

