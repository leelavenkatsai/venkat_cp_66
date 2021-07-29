# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.


def isrotation(x, y):
    # Your code goes here
    s1 = len(str(x))
    s2 = len(str(y))
    tmp = ''
    # Check if sizes of two strings are same
    if s1 != s2:
        return False
    # Create a temp string with value str1.str1
    tmp = str(x) + str(x)
    if (tmp.count(str(y)) > 0):
        return True
    elif(str(y)[::-1] == str(x) or str(x)[::-1] == str(y)):
        return True
    else:
        return False