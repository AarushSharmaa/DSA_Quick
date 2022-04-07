# Flashcards for DSA Revision 

## Heaps

For a 0-indexed array : 

- **Arr[(i - 1) / 2]**	Returns the parent node
- **Arr[(2 * i) + 1]**	Returns the left child node
- **Arr[(2 * i) + 2]**	Returns the right child node
- If n is the length of the array, **(n-1)//2** will be the last non-leaf node
- In python, we use heapq module to implement minHeap and maxHeap.

**Time and Space Complexity**:
- Building Heap - O(N) Time and O(1) Space
- Insertion - O(log(N)) Time
- Deletion - O(log(N)) Time


## Key Points : 

- The Python priority queue is built on the heapq module, which is basically a binary heap.
- When we use heapq to to implement priority queue, by default, it behaves as a min heap.
- If we have a declared array named as heap, we can use below methods : 
- heapify(heap), heappush(heap, x), heappop(heap), heappushpop(heap, 8), nlargest(k, heap), nsmallest(k, heap)



# Searching 

## Key Points : 
- Binary Search Algorithm reduces search space by a larger unit as compared to Linear Scan.
- Works in problems like First and Last Occurence, Searching in Sorted Rotated Array, Square Root, Peak Element and so on.


# Sorting
