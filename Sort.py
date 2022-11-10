import numpy as np
import time
import random


def generate_array(dim, range_n):
    return np.random.randint(range_n+1, size=dim)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


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
            swap(arr, i, j)
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
    swap(arr, p, i)
    return partition(arr, p, r)


def _heap_size(arr):
    i = 0
    while arr[i] is not None:
        if i == len(arr)-1:
            return (i+1)
        i += 1
    return i


def heapify(arr, i):
    l = (i*2)+1
    r = (i*2)+2
    if l < heap_size and arr[l] > arr[i]:
        largest = l
    else:
        largest = i

    if r < heap_size and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)


def build_heap(arr):
    lenght = heap_size
    for i in range((lenght//2)-1, -1, -1):
        heapify(arr, i)


def heap_sort(arr):
    build_heap(arr)
    global heap_size
    for i in range(len(arr)-1, 0, -1):
        swap(arr, 0, i)
        heap_size -= 1
        heapify(arr, 0)


def iterative_quick_sort(arr, p, r):
    while p < r:
        q = partition(arr, p, r)
        if q-p < r-q:
            iterative_quick_sort(arr, p, q)
            p = q+1
        else:
            iterative_quick_sort(arr, q+1, r)
            r = q


dim = 1000000
range_n = 2000000
b = [0] * dim

'''
for i in range(33):
    heap[i] = np.random.randint(range_n+1)

start = time.time()
build_heap(heap)
end = time.time()
print(end - start)
print()

b = BstNode(heap[0])
for i in range(1, heap_size(heap)):
    b.insert(heap[i])
b.display()

# print_heap(heap)


i = 0
while heap[i] is not None:
    print(heap[i])
    i += 1


print("INSERT SORT")
arr = generate_array(dim, range_n)
start = time.time()
sorted_arr = insertion_sort(arr)
end = time.time()
print(end - start)
print()
'''

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


print("ITERATIVE QUICK SORT")
arr = generate_array(dim, range_n)
start = time.time()
iterative_quick_sort(arr, 0, len(arr)-1)
end = time.time()
print(end - start)
print()


print("HEAP SORT")
arr = generate_array(dim, range_n)
heap_size = _heap_size(arr)
start = time.time()
heap_sort(arr)
end = time.time()
print(end - start)
print()
