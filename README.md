# Sorting Algorithms in Python

This repository contains Python implementations of the most commonly used sorting algorithms. Each program accepts user input, measures execution time, and displays the algorithm's time and space complexity.

## Algorithms Included

1. Bubble Sort
2. Insertion Sort
3. Selection Sort
4. Merge Sort
5. Quick Sort

---

# 1. Bubble Sort

## Description
Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order. The process continues until the array becomes sorted.

### Time Complexity

| Case | Complexity |
|------|------------|
| Best | O(n) |
| Average | O(n²) |
| Worst | O(n²) |

### Space Complexity

O(1)

### Advantages
- Easy to understand
- Good for small datasets
- Detects already sorted arrays

### Disadvantages
- Slow for large datasets
- Performs many unnecessary comparisons

---

# 2. Insertion Sort

## Description
Insertion Sort builds the sorted array one element at a time by inserting each element into its correct position.

### Time Complexity

| Case | Complexity |
|------|------------|
| Best | O(n) |
| Average | O(n²) |
| Worst | O(n²) |

### Space Complexity

O(1)

### Advantages
- Efficient for small datasets
- Stable sorting algorithm
- Works well for nearly sorted arrays

### Disadvantages
- Inefficient for large datasets

---

# 3. Selection Sort

## Description
Selection Sort repeatedly finds the smallest element from the unsorted portion and places it at the beginning.

### Time Complexity

| Case | Complexity |
|------|------------|
| Best | O(n²) |
| Average | O(n²) |
| Worst | O(n²) |

### Space Complexity

O(1)

### Advantages
- Simple implementation
- Performs fewer swaps

### Disadvantages
- Always performs O(n²) comparisons
- Not suitable for large datasets

---

# 4. Merge Sort

## Description
Merge Sort is a Divide and Conquer algorithm. It divides the array into two halves, recursively sorts them, and merges the sorted halves.

### Time Complexity

| Case | Complexity |
|------|------------|
| Best | O(n log n) |
| Average | O(n log n) |
| Worst | O(n log n) |

### Space Complexity

O(n)

### Advantages
- Fast and stable
- Suitable for large datasets
- Guaranteed O(n log n)

### Disadvantages
- Requires extra memory

---

# 5. Quick Sort

## Description
Quick Sort is a Divide and Conquer algorithm that selects a pivot element and partitions the array into smaller and larger elements before recursively sorting them.

### Time Complexity

| Case | Complexity |
|------|------------|
| Best | O(n log n) |
| Average | O(n log n) |
| Worst | O(n²) |

### Space Complexity

- O(log n) (Recursive Stack)
- O(n) for implementations that create new lists

### Advantages
- Very fast in practice
- Efficient for large datasets
- Widely used

### Disadvantages
- Worst case O(n²)
- Performance depends on pivot selection

---

# Execution Time

Each program measures execution time using Python's built-in `time.perf_counter()` function.

Example:

```python
import time

start_time = time.perf_counter()

# Sorting algorithm

end_time = time.perf_counter()

print("Execution Time:", end_time - start_time)
```

---

# User Input Format

Enter numbers separated by spaces.

Example:

```
10 5 3 8 2 1
```

---

# Example Output

```
Sorted Array: [1, 2, 3, 5, 8, 10]

Execution Time: 0.0000123000 seconds

Time Complexity:
Best Case    : O(n log n)
Average Case : O(n log n)
Worst Case   : O(n²)

Space Complexity: O(log n)
```

---

# Complexity Comparison

| Algorithm | Best | Average | Worst | Space |
|-----------|------|----------|--------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |

---

# Requirements

- Python 3.x

No external libraries are required.

---

# Author

**Sayyed Asif (CSE AI & ML)**
**92460118359**
**5EN12**

---

