# in this, we do it same as the selection sort, except for a few differences.
# in selection sort,we chose the minimum and moved it to left most, and then again same continued.
# here, it's a bit different bcoz, we go as the numbers are placed and keep moving them to the left.
# While comparing, we just keep arranging according to the sorted part in left.


# time complexity  = O(N^2)
# space complexity = O(1) bcoz it doesn't require any extra space
# Pros -> Less space, Easy to implement(Only 2 for loops)
# Cons -> Very high time complexity, do not use when time is a concern


def insertion_sort(anylist):
    for i in range(1,len(anylist)):
        key = anylist[i]
        j = i-1
        while j>=0 and key < anylist[j]:
            anylist[j+1] = anylist[j]
            j-=1
        anylist[j+1] = key
    return anylist


import random as rand
#generating 100 random numbers for an unsorted list which we'll sort.
randomlist = rand.sample(range(1,1000),100)
print(randomlist)
print(insertion_sort(randomlist))
