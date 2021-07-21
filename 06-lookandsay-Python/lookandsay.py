# Write the function lookAndSay(a) that takes a list of numbers and returns a list of numbers
# that results from "reading off" the initial list using the look-and-say method, using tuples 
# for each (count, value) pair.
# 
# For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

def readArray():
    a = []
    l = int(input())
    for i in range(l):
        a.append(int(input()))
    return a

def lookAndSay(a):
    Intfreq=[]
    initial=1
    count=0 
    if(len(a)==0):
        return []
    while(True):
        if(len(a)-1 == count):
            Intfreq.append((initial,a[count]))
            break
        elif(a[count]==a[count+1]):
            count=count+1
            initial=initial+1
        else:
            Intfreq.append((initial,a[count]))
            initial=1
            count=count+1
    return Intfreq
    

#lookAndSay(readArray())


