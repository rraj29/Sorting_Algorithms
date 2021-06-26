# Also called "Sinking Sort"
# Basically, we repeatably compare each pair of adjacent items,
# and swap them if they are in wrong order.

# time complexity  = O(N^2)
# space complexity = O(1) bcoz it doesn't require any extra space
# Pros -> Less space, Easy to implement(Only 2 for loops)
# Cons -> Very high time complexity, do not use when time is a concern

def bubble_sort(anylist):
    # for i in range(len(anylist)-1,-1,-1):     #this is also one of the ways to do it. the iteration starts from right.
    #     for j in range(i,len(anylist)-1):
    for i in range(len(anylist)-1):         #in this one,the largest number reaches the end in 1st iteration
        for j in range(len(anylist)-i-1):   # 2nd largest in 2nd iteration, and so on
            if anylist[j] > anylist[j+1]:
                anylist[j], anylist[j+1] = anylist[j+1], anylist[j]
    print(anylist)


import random as rand
#generating 100 random numbers for an unsorted list which we'll sort.
randomlist = rand.sample(range(1,1000),100)
print(randomlist)
bubble_sort(randomlist)



