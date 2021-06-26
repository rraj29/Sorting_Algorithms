# divide and conquer algorithm
# Unlike merge sort, it does NOT require extra space

# we sort the elements based on "PIVOT" that we select
# the rightmost element is generally selected as the pivot.

import random as rand


def partition(custom_list, low, high):  # for the markers 'left' and 'right'
    i = low - 1
    pivot = custom_list[high]
    for j in range(low, high):
        if custom_list[j] <= pivot:
            i += 1
            custom_list[i], custom_list[j] = custom_list[j], custom_list[i]
    custom_list[i + 1], custom_list[high] = custom_list[high], custom_list[i + 1]
    return i+1


def quick_sort(custom_list, low, high):
    if low < high:
        pi = partition(custom_list, low, high)
        quick_sort(custom_list, low, pi - 1)
        quick_sort(custom_list, pi + 1, high)
    return custom_list


randomlist = rand.sample(range(1, 1000), 100)
print(randomlist)
print(quick_sort(randomlist, 0, len(randomlist) - 1))
