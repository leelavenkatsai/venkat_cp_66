# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	if(k>=3):
		return 0
	if(digit< 0):
		digit = digit*-1
		v = digit//(10**k)
		n = v%10
		return n
	else:
		v1 = digit//(10**k)
		n1 = v1%10
		return n1 
