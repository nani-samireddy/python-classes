import math as M
def isPerfect(number):
    res = 1
    sqrt = int(M.sqrt(number))
    for i in range(2,sqrt+1):
        if(number%i == 0):
            res += (i + (number//i))
    return res==number

t = int(input())
for _ in range(0,t):
    num = int(input())
    print(isPerfect(num))



def isSpy(number):
    sum = 0
    prod = 1
    for digit in number:
        sum +=int(digit)
        prod *=int(digit)
    return sum==prod
