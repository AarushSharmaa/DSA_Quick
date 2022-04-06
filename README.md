# Heaps


# Flashcards for DSA Revision 

## Heaps
For a 0-indexed array

- **Arr[(i - 1) / 2]**	Returns the parent node
- **Arr[(2 * i) + 1]**	Returns the left child node
- **Arr[(2 * i) + 2]**	Returns the right child node
- If n is the length of the array, **(n-1)//2** will be the last non-leaf node


- In-Built Methods to implement MinHeap and MaxHeap :

**Code :**

import heapq

l1 = [5, 7, 9, ,1 3]

heapq.heapify(l1)

l1 = [1, 3, 9, 7 , 5] --> A min heap

- The Python priority queue is built on the heapq module, which is basically a binary heap.
- When we use heapq to to implement priority queue, by default, it behaves as a min heap.
- If we have a declared array named as heap, we can use below methods : 
- heapify(heap), heappush(heap, x), heappop(heap), heappushpop(heap, 8), nlargest(k, heap), nsmallest(k, heap)

# Searching 
