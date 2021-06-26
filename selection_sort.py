# Almost similar to bubble sort

# in this, we go in a loop, and keep creating sorted lists.
# in first iteration, the smallest reaches the 1st position.
# next iteration starts from 2nd place, and hence the now smallest(actual 2nd smallest) reaches the second position.
# And so on

# time complexity  = O(N^2)
# space complexity = O(1) bcoz it doesn't require any extra space
# pros -> space efficient, easy to implement
# Cons -> Very high time complexity, do not use when time is a concern
# better to use only for small lists where the numbers are in a highly randomised order


def selection_sort(anylist):
    for i in range(len(anylist)):                   #----------------- O(n)
        min_index = i
        for j in range(i+1, len(anylist)):           #----------------- O(n)
            if anylist[min_index] > anylist[j]:
                min_index = j
        anylist[i], anylist[min_index] = anylist[min_index], anylist[i]
    print(anylist)


import random as rand
#generating 100 random numbers for an unsorted list which we'll sort.
randomlist = rand.sample(range(1,1000),100)
print(randomlist)
selection_sort(randomlist)


