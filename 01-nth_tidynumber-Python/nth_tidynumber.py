# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def fun_nth_tidynumber(n):
    # return 0
    count=0
    i=0
    while count<=n:
        i+=1
        if (isTidy(i)):
            count+=1
    return i
def isTidy(value):
    p = 10
    while (value):
        r = value % 10
        value //= 10
        if r > p:
            return False
        p = r
    return True