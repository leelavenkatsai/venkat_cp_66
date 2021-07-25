# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).



def fun_nth_happy_prime(n):
	# return 0
	j = 0
	k = 0
	while(j<= abs(n)):
		k +=1
		if(happyPrime(k)):
			j+=1
	return k

def happyPrime(n):
	if(prime(n)==True and happyNum(n)==True):
		return True
	return False

def happyNum(n):
	m = 0
	while(n!=0):
		m += (n%10)**2
		n//=10
	if m == 1:
		return True
	elif m<10:
		return False
	else:
		return happyNum(m)

def prime(n):
	if n<2:
		return False
	for i  in range(2,n):
		if(n%i ==0):
			return False
		return True
