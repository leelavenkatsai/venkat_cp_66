# Background:  in Chess, a King can move from any square to
# any adjacent square.  A King’s Tour is a series of legal King
# moves so that every square is visited exactly once. 
# We can represent a Kings Tour in a 2d list where the 
# numbers represent the order the squares are visited, going 
# from 1 to N2.  For example, consider these 2d lists:

#    [ [  3, 2, 1 ],    	[ [  1, 2, 3 ],  	[ [ 3, 2, 1 ],
#  	[  6, 4, 9 ],      	[  7, 4, 8 ],    	[ 6, 4, 0 ],
#  	[  5, 7, 8 ] ]     	[  6, 5, 9 ] ]   	[ 5, 7, 8 ] ]

# The first is a legal Kings Tour but the second is not, 
# because there is no way to legally move from the 7 to the 8, 
# and the third is not, because it contains a 0 which is out
#  of range.  With this in mind, write the function 
# isKingsTour(board) that takes a 2d list of integers, 
# which you may assume is NxN for some N>0, and 
# returns True if it represents a legal Kings Tour 
# and False otherwise.
def position(a,b):
    l=[0,0]
    for i in range(len(a)):
        for j in range(len(a[0])):
            if(b==a[i][j]):
                l[0]=i
                l[1]=j
    return l
def isKingsTour(L):
    n=len(L)
    k=len(L[0])
    f=n*k
    for i in range(1,f):
        a1=position(L,i)
        a2=position(L,i+1)
        m=abs(a1[0]-a2[0])
        c=abs(a1[1]-a2[1])
        if(m==1 and c==0):
            continue
        elif(m==0 and c==1):
            continue
        elif(m==1 and c==1):
            continue
        else:
            return False
    return True
