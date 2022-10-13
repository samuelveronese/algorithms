import random


def unsorted_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


def rand_unsorted_search(arr, x):
    n = len(arr)
    s = random.randrange(0, n-1)
    for i in range(n):
        j = (i+s) % n
        if arr[j] == x:
            return j
    return -1


#arr = random.sample(range(1, 100), 70)
arr = [2, 7, 3, 1, 5, 2]
print(rand_unsorted_search(arr, 2))
