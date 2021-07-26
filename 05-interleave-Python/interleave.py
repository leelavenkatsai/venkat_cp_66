# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



def fun_interleave(s1,s2):
	# return ""
	s3 = ""
	for i in range(len(s1)):
		for j in range(i,len(s2)):
			s3 += s1[i] + s2[j]
			break
	if len(s1) > len(s2):
		s3 += s1[len(s1) - (len(s1)-len(s2)) : len(s1)]
	if len(s2) > len(s1):
		s3 += s2[len(s2) - (len(s2) - len(s1)) : len(s2)]
	return s3
	