# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	# pass
	n = abs(n)
	if (n ==0 ):
		return False
	while n!=0:
		a = n%10
		n = n//10
		b = n%10
		if (a==b):
			return True
	return False