import numpy as np
import time
import random


def generate_array(dim, range_n):
    return np.random.randint(range_n, size=dim)


def insertion_sort(arr):
    for j in range(1, len(arr), 1):
        key = arr[j]
        i = j-1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
    return


def merge_sort(arr, p, r):
    if p >= r:
        return
    q = (p+r)//2
    merge_sort(arr, p, q)
    merge_sort(arr, q+1, r)
    merge(arr, p, q, r)


def merge(arr, p, q, r):
    i = 0
    j = p
    k = q+1
    while j <= q or k <= r:
        if j <= q and (k > r or arr[j] <= arr[k]):
            b[i] = arr[j]
            j += 1
        else:
            b[i] = arr[k]
            k += 1
        i += 1
    for i in range(r-p+1):
        arr[p+i] = b[i]


def quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q)
        quick_sort(arr, q+1, r)
    return


def partition(arr, p, r):
    x = arr[p]
    i = p-1
    j = r+1
    while True:
        while True:
            j -= 1
            if arr[j] <= x:
                break
        while True:
            i += 1
            if arr[i] >= x:
                break
        if i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        else:
            return j


def rand_quick_sort(arr, p, r):
    if p < r:
        q = rand_partition(arr, p, r)
        quick_sort(arr, p, q)
        quick_sort(arr, q+1, r)
    return


def rand_partition(arr, p, r):
    i = random.randrange(p, r+1)
    temp = arr[p]
    arr[p] = arr[i]
    arr[i] = temp
    return partition(arr, p, r)


dim = 1000
range_n = 100
b = [0] * dim


print("INSERT SORT")
arr = generate_array(dim, range_n)
start = time.time()
sorted_arr = insertion_sort(arr)
end = time.time()
print(end - start)
print()


print("MERGE SORT")
arr = generate_array(dim, range_n)
start = time.time()
merge_sort(arr, 0, len(arr)-1)
end = time.time()
print(end - start)
print()


print("QUICK SORT")
arr = generate_array(dim, range_n)
start = time.time()
quick_sort(arr, 0, len(arr)-1)
end = time.time()
print(end - start)
print()


print("RANDOM START QUICK SORT")
arr = generate_array(dim, range_n)
start = time.time()
rand_quick_sort(arr, 0, len(arr)-1)
end = time.time()
print(end - start)
print()
