## Flashcards for DSA Revision 

# Heaps

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


## Key Points : 

* Sorting algorithms are mainly of two types:

* Comparison based sorting - In this type of algorithm, we need to compare the array elements with each other in order to sort them. They are generally O(N2) or O(NlogN) algorithms. Eg. Insertion sort, Bubble sort etc.  
* Non-comparison based sorting - This type of sorting algorithm does not involve comparison between elements.


# Binary Tree : 

## Key Points : 
- For a tree with n nodes, there will be n-1 edges.
- Categories of Tree : Rooted vs Unrooted, Skewed, Binary
- For a Perfect Binary Tree with N nodes, maximum number of levels : O(log(N))
- If total number of levels is i, total number of nodes = 2^(i+1) - 1 [levels are 0 ordered] -> For a Perfect Binary Tree
- For mirror image of a Binary Tree, just swap left and right nodes at each step.
- Symmetric Check : Check if LST and RST are mirror images of each other. If they are : **Symmetric**

# Binary Search Tree : 

# Recursion : 

- **Pass by Value** : When you pass a copy of the variable to a function and original value remains unchanged.
- **Pass by Reference** : When you pass the memory address of the variable and not its copy. 
- Visualising Recursive Tree Diagram is important for each solution.
