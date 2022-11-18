import random


class Sort:

    def __init__(self):
        self = self

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def insertion_sort(self, arr):
        for j in range(1, len(arr), 1):
            key = arr[j]
            i = j-1
            while i >= 0 and arr[i] > key:
                arr[i+1] = arr[i]
                i -= 1
            arr[i+1] = key

    def merge_sort(self, arr):
        self.b = [0]*len(arr)
        self._merge_sort(arr, 0, len(arr)-1)

    def _merge_sort(self, arr, p, r):
        if p >= r:
            return
        q = (p+r)//2
        self._merge_sort(arr, p, q)
        self._merge_sort(arr, q+1, r)
        self.merge(arr, p, q, r)

    def merge(self, arr, p, q, r):
        i = 0
        j = p
        k = q+1
        while j <= q or k <= r:
            if j <= q and (k > r or arr[j] <= arr[k]):
                self.b[i] = arr[j]
                j += 1
            else:
                self.b[i] = arr[k]
                k += 1
            i += 1
        for i in range(r-p+1):
            arr[p+i] = self.b[i]

    def quick_sort(self, arr):
        self._quick_sort(arr, 0, len(arr)-1)

    def _quick_sort(self, arr, p, r):
        if p < r:
            q = self.partition(arr, p, r)
            self._quick_sort(arr, p, q)
            self._quick_sort(arr, q+1, r)
        return

    def partition(self, arr, p, r):
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
                self.swap(arr, i, j)
            else:
                return j

    def rand_quick_sort(self, arr):
        self._rand_quick_sort(arr, 0, len(arr)-1)

    def _rand_quick_sort(self, arr, p, r):
        if p < r:
            q = self.rand_partition(arr, p, r)
            self._quick_sort(arr, p, q)
            self._quick_sort(arr, q+1, r)
        return

    def rand_partition(self, arr, p, r):
        i = random.randrange(p, r+1)
        self.swap(arr, p, i)
        return self.partition(arr, p, r)

    def _heap_size(arr):
        i = 0
        while arr[i] is not None:
            if i == len(arr)-1:
                return (i+1)
            i += 1
        return i

    def heapify(self, arr, i):
        l = (i*2)+1
        r = (i*2)+2
        if l < self.heap_size and arr[l] > arr[i]:
            largest = l
        else:
            largest = i

        if r < self.heap_size and arr[r] > arr[largest]:
            largest = r

        if largest != i:
            self.swap(arr, i, largest)
            self.heapify(arr, largest)

    def build_heap(self, arr):
        lenght = self.heap_size
        for i in range((lenght//2)-1, -1, -1):
            self.heapify(arr, i)

    def heap_sort(self, arr):
        self.heap_size = len(arr)
        self.build_heap(arr)
        for i in range(len(arr)-1, 0, -1):
            self.swap(arr, 0, i)
            self.heap_size -= 1
            self.heapify(arr, 0)

    def iterative_quick_sort(self, arr):
        self._iterative_quick_sort(arr, 0, len(arr)-1)

    def _iterative_quick_sort(self, arr, p, r):
        while p < r:
            q = self.partition(arr, p, r)
            if q-p < r-q:
                self._iterative_quick_sort(arr, p, q)
                p = q+1
            else:
                self._iterative_quick_sort(arr, q+1, r)
                r = q

    def counting_sort(self, arr):
        self.b = [0]*len(arr)
        self._counting_sort(arr, max(arr))

    def _counting_sort(self, arr, k):
        c = [0]*(k+1)
        for j in range(len(arr)):
            c[arr[j]] += 1
        for i in range(1, k):
            c[i] += c[i-1]
        for j in range(len(arr)-1, -1, -1):
            self.b[c[arr[j]]-1] = arr[j]
            c[arr[j]] -= 1

    def radix_sort(self, arr):
        self._radix_sort(arr, len(str(max(arr))))

    def _radix_sort(self, arr, d):
        for i in range(d):
            self._counting_sort(arr, 9)
            for j in range(len(arr)):
                arr[j] = arr[j]//10

    def bucket_sort(self, arr):
        self._bucket_sort(arr, max(arr))

    def _bucket_sort(self, arr, k):
        n = len(arr)
        b = [[] for i in range(n)]
        for j in range(n):
            b[arr[j]//k].append(arr[j])
        for i in range(n):
            self.insertion_sort(b[i])
        i = 0
        for j in range(n):
            for l in range(len(b[j])):
                arr[i] = b[j][l]
                i += 1
