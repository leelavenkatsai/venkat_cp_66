# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

def nthCircularPrime(x):
    count=0
    n=2
    while (count<x):
        if(isPrime(n) and circular(n)):
            count+=1
        n+=1
    return n-1

def digitCount(n):
    n =abs(n)
    count=0
    while n!=0:
        count+=1
        n = n // 10
    return count

def rotate(x):
    count=digitCount(x)
    sum=x%10*10**(count-1)+x//10
    return sum

def circular(n):
    len = digitCount(n)
    if (len == 1):
        return True
    else:
        cnt=0
        while cnt<len:
            if(not isPrime(n)):
                return False
            n=rotate(n)
            cnt=cnt+1
            if cnt == len:
                return True
    return False

def isPrime(n):
        if (n < 2):
            return False
        for value in range(2,n):
            if (n % value == 0):
                return False
        return True