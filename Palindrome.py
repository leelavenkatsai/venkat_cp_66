def isPalindrome(n):
	reverse= int(str(n)[::-1])
	if(int(n)==reverse):
		return(True)
	else:
		return(False)

def isPrime(n):
	if n> 1:	
		for i in range(2, int(n/2)+1):
			if (n % i) == 0:
				print(False)
				#break
			else:
				return (True)
	else:
		return(False)

def isPalindromicPrime(n):
	if (isPalindrome(n)):
		if (isPrime(n)):
			return True
	else:	
		return False

print((isPalindromicPrime(10)))
print((isPalindromicPrime(104)))
print((isPalindromicPrime(235)))
print((isPalindromicPrime(131)))
# print((isPalindromicPrime(900))
# print((isPalindromicPrime(101))
# print((isPalindromicPrime(383))
# print((isPalindromicPrime(373))
# print((isPalindromicPrime(121))