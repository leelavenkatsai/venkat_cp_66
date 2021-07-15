# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or int values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	a = (int((x2-x1)**2) + int((y2-y1)**2))
	b = (int((x3-x1)**2) + int((y3-y1)**2))
	c = (int((x3-x2)**2) + int((y3-y2)**2))
	if((a > 0 and b > 0 and c > 0) and (a == (b + c) or b == (a + c) or c == (b + c))):
		return True
	else:
		return False
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# x3 = int(input())
# y3 = int(input())