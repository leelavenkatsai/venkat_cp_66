# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly 
# a non-negative integer n and k and returns the list that 
# contains k number of subsets from the power set as sets. 
# (The values in the set will range from 1 to n).
# Example:
# 	limitedPowerSet(5, 7) => 
# [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]

def limitedPowerSet(n, k):
    # Your code goes here...
    # pass
    l=[]
    for i in range(n+1):
        for j in range(k):
            if(j==0):
                s=set({})
                l.append(s)
            else:
                s=set({j})
                l.append(s)
            if(len(l)==k):
                print(l)
                return l