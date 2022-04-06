#1.
#Brute Force to build a max heap from a given array - O(N*log(N)) Time and O(1) Space
"""
arr = [2,4,1,3]

n = len(arr)

for i in range(0, n):

    j = i
    while (j > 0 and arr[j] > arr[(j-1)//2]):

            arr[j], arr[(j-1)//2] = arr[(j-1)//2], arr[j]

            j  = (j - 1)// 2

print(arr)
"""

#2
#Optimal Method to build a max-heap - O(N) Time and O(1) Space
"""
def heapify(arr, n, i):
    largest = i

    left = 2*i+1
    right = 2*i+2

    if left<n and arr[left]>arr[largest]:
        largest = left

    if right<n and arr[right]>arr[largest]:
        largest = right

    if largest!=i:
        arr[largest], arr[i] = arr[i], arr[largest]

        heapify(arr, n, largest)

def buildHeap(arr):
    n=len(arr)

    start = n//2 - 1
    for i in range(start, -1, -1):
        heapify(arr, n, i)

    return arr

arr = [2, 4, 1, 3]
print(buildHeap(arr))
"""

#3
#Build a min-heap - same as above with minor differences

#4
#print k largest elements - O(N + k*log(N)) Time and O(1) Space
"""
import heapq

def kLargest(li, n, k):

    heapq.heapify(li)
    return heapq.nlargest(k, li)

li = [2,3,4,1,9]
k = 2
n = len(li)
print(kLargest(li, n, k))
"""

#5
#print k smallest elements - O(N + k*log(N)) Time and O(1) Space
"""
import heapq
def ksmallest(li, n, k):

    heapq.heapify(li)
    return heapq.nsmallest(k, li)

li = [2,3,4,1,9]
k = 2
n = len(li)
print(ksmallest(li, n, k))
"""

#6
#heap sort - 0(N*log(N)) Time and O(1) Space
"""
def heapify(arr, n, i):
    smallest = i

    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[smallest]:
        smallest = left
    if right < n and arr[right] > arr[smallest]:
        smallest = right

    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]

        self.heapify(arr, n, smallest)

    # Function to build a Heap from array.


def buildHeap(arr, n):
    start = n // 2 - 1
    for i in range(start, -1, -1):
        self.heapify(arr, n, i)


def HeapSort(arr, n):
    self.buildHeap(arr, n)

    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        self.heapify(arr, i, 0)

    return arr

arr = [9, 1, 7, 3, 4]
n = len(arr)
HeapSort(arr, n)
print(arr)
"""

#7
#k-closest points on X-Y plane

#8
#tying ropes

#9
#merge sorted arrays
"""
def mergeKArrays(arr, K):

    import heapq
    heap = []
    for i in range(0, len(arr)):
        heapq.heappush(heap, (arr[i][0], i, 0))

    count = 0
    final = []
    while count < K * K:
        magnitude, i, j = heapq.heappop(heap)
        final.append(magnitude)
        if (j + 1) < len(arr):
            heapq.heappush(heap, (arr[i][j + 1], i, j + 1))
        count += 1
    return final
"""

#10
#kth smallest sum pairs
"""
def kSmallestPairs(nums1, nums2, k):
    heap = []
    for i in range(len(nums1)):
        heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

    final = []
    count = 0
    while (heap and count < k):
        sums, i, j = heapq.heappop(heap)
        final.append([nums1[i], nums2[j]])
        if (j + 1 < len(nums2)):
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        count += 1

    return final
import heapq
nums1 = [2,3,4]
nums2 = [1,5,7,8]
k = 2
ans = kSmallestPairs(nums1, nums2, k)
print(ans)
"""

#11
#kth smallest in special matrix
"""
def ksmallest(matrix, k):
    heap = []
    for i in range(0, len(matrix)):
        heapq.heappush(heap, (matrix[i][0], i, 0))
    answer = 0
    count = 0
    while heap and count < k:
        answer, i1, j1 = heapq.heappop(heap)
        if (j1 + 1) < len(matrix):
            heapq.heappush(heap, (matrix[i1][j1 + 1], i1, j1 + 1))
        count += 1
    return answer


import heapq
matrix = [[1,5,9],
          [10,11,13],
          [12,13,15]]
k = 8
ans = ksmallest(matrix, k)
print(ans)
"""

#12
#Numbers with Limited Prime Factors - 1
"""
def limitedprime(n):
    heap = []

    #implement the first sure contender
    heapq.heappush(heap, 1)
    count = 0
    d = {} #in order to avoid duplicates

    while (heap and count < n):
        i = heapq.heappop(heap)
        #now we will add next possible contenders - 2*i, 3*i, 5*i

        if (2*i) in d:
            pass
        else:
            d[2*i] = 2*i
            heapq.heappush(heap, 2*i)
        if (3*i) in d:
            pass
        else:
            d[3*i] = 3*i
            heapq.heappush(heap, 3*i)
        if (5*i) in d:
            pass
        else:
            d[5*i] = 5*i
            heapq.heappush(heap, 5*i)
        count += 1
    return i

n = 10
import heapq
ans = limitedprime(n)
print(ans)
"""

#13

#Numbers with Limited Prime Factors - 2
"""
def nthSuperUglyNumber(n, primes):
    heap = []
    import heapq
    heapq.heappush(heap, 1)

    count = 0
    d = {}
    while (heap and count < n):
        answer = heapq.heappop(heap)

        for prime in primes:
            if prime in d:
                pass
            else:
                d[prime] = prime
                heapq.heappush(heap, prime * answer)
                print(count)
        count += 1

    return answer

n = 1
primes = [2,3,5]
ans = nthSuperUglyNumber(n, primes)
print(ans)
"""


