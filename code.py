
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

def getNextPrime(number):
    while isPrime(number+1):
        number=number+1
    return number
    
def isSPrime(number):
    firstPrime = 2
    secondPrime = 3
    
    res=True
    while(True):
        prod = firstPrime * secondPrime
        print(firstPrime,secondPrime,prod)
        sum1 = firstPrime + secondPrime
        if sum1 >= number:
            res = False
            break
        else:
            if prod == number:
                res =True
                break
            elif prod < number:
                secondPrime = getNextPrime(number)
            else:
                firstPrime = getNextPrime(number)
    return res
    
        
    
t = int(input())
for _ in range(0,t):
    num = int(input())
    print(isSPrime(num))

