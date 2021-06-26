# Here, we create buckets and distribute the elements in the buckets
# sort the elements within the buckets
# then, simply merge the buckets

# Number of buckets = round(sqrt(total no. of elements))
# Appropriate bucket for any element(value)  = ceil(Value * No. of Buckets/Max Value in the array)
# ceil= ceiling function, round = round off, sqrt = square root

# time complexity = O(N^2)
# space complexity = O(N)
# Use when the numbers are uniformly distributed. e.g-( 1,2 4,5,3,9,7,8)
# NOT WHEN e.g-( 1,23,400,53,9,7000,8)

import random as rand                       # for the randomlist
import math                                 # for sqrt function
# from insertion_sort import insertion_sort   # importing insertion sort, so easy to sort the array directly


def insertion_sort(anylist):
    for i in range(1,len(anylist)):
        key = anylist[i]
        j = i-1
        while j>=0 and key < anylist[j]:
            anylist[j+1] = anylist[j]
            j-=1
        anylist[j+1] = key
    return anylist


def bucket_sort(anylist):
    number_of_buckets = round(math.sqrt(len(anylist)))
    maxValue = max(anylist)
    arr = []

    for i in range(number_of_buckets):
        arr.append([])                  # creating the required number of buckets

    for j in anylist:                   # getting the bucket number in which the element should go
        index_bucket = math.ceil((j * number_of_buckets) / maxValue)
        arr[index_bucket-1].append(j)   # adding the element to the calculated bucket

    for i in range(number_of_buckets):
        arr[i] = insertion_sort(arr[i])      # sorting the elements in each bucket

    k = 0
    for i in range(number_of_buckets):
        for j in range(len(arr[i])):
            anylist[k] = arr[i][j]
            k +=1
    return anylist


randomlist = rand.sample(range(1,1000),100)
print(randomlist)
print(bucket_sort(randomlist))

