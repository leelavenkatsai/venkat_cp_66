# fabricyards(inches)
# Fabric must be purchased in whole yards, so purchasing just 1 inch 
# of fabric requires purchasing 1 entire yard. With this in mind, 
# write the function fabricYards(inches) that takes the number of 
# inches of fabric desired, and returns the smallest number of whole 
# yards of fabric that must be purchased.

# fabricexcess(inches)
# Write the function fabricexcess(inches) that takes the number of 
# inches of fabric desired and returns the number of inches of excess 
# fabric that must be purchased (as purchases must be in whole yards).
# Hint: you may want to use fabricyards, which you just wrote!


def fabricyards(inches):
	# Your code goes here...
	# return 1
	if (inches == 0):
		return 0
	elif(inches % 36 == 0):
		p = int(inches // 36)
		return p
	else:
		p = (int(inches // 36)+1)
		return p

def fabricexcess(inches):
	# Your code goes here...
	# return 1
	if (inches == 0):
		return inches
	elif(inches % 36 == 0):
		p = (inches // 36)
		# return p
	else:
		p = (int(inches // 36)+1)
		# return p
	return ((p*36) - inches)