def isprime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def digits1(n):
    s1 = 0
    while (n > 0):
        s1 += n % 10
        n = n // 10
    return s1


def isadditiveprime(n):
    # Your code goes here
    if isprime(n):
        s1 = digits1(n)
        if isprime(s1):
            return True
    return False

print(isadditiveprime(5))
print(isadditiveprime(13))