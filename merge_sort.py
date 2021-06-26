# based on divide and conquer principle
# divide them into half, and keep dividing them recursively until they can no longer be divided
# now merge the halves by sorting them

# time complexity - O(Nlog(N))
# space complexity - O(N)
# overall good algorithm


import random as rand

def merge(customList, left, middle, right):
    n1 = middle - left + 1      # no. of elements in the first sub-array
    n2 = right - middle         # no. of elements in the first sub-array

    L = [0] * (n1)              # creating 1st sub-array
    R = [0] * (n2)              # creating 2nd sub-array

    for i in range(n1):
        L[i] = customList[left + i]
    for j in range(n2):
        R[j] = customList[middle + 1 + j]

    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] < R[j]:
            customList[k] = L[i]
            i+=1
        else:
            customList[k] = R[j]
            j+=1
        k+=1
    while i < n1:
        customList[k] = L[i]
        i+=1
        k+=1
    while j < n2:
        customList[k] = R[j]
        j+=1
        k+=1


def merge_sort(customList, left, right):
    if left < right:
        middle = (left + right - 1)//2
        merge_sort(customList, left, middle)
        merge_sort(customList, middle+1, right)
        merge(customList, left, middle, right)
    return customList


randomlist = rand.sample(range(1,1000),100)
print(randomlist)
print(merge_sort(randomlist,0,99))
