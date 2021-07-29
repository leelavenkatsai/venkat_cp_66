# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	# your code goes here
	# pass
	if(a==[]):
		return None
	b = len(a)
	if(b!=0):
		if(b%2 !=0):
			return a[b//2]
		else:
			set1= a[b//2]
			set2= a[b//2-1]
			value = (set1 + set2)/2
			return value
	else:
		return None