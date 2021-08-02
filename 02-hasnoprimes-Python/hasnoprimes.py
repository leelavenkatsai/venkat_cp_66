# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.


def fun_hasnoprimes(l):
	# return True
    a=[]
    for row in l:
        for col in row:
            if(noPrime(col)==False):
                return False
    return True
def noPrime(a):
    if(a==0 or a==2):
        return False
    if(a>=1):
        for i in range(2,a):
            if(a%i==0):
                return True
        return False

