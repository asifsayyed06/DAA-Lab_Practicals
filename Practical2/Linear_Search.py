import time

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Input
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

target = int(input("Enter the element to search: "))

# Start timer
start_time = time.perf_counter()

result = linear_search(arr, target)

# End timer
end_time = time.perf_counter()

# Output
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

# Execution Time
print(f"Execution Time: {end_time - start_time:.10f} seconds")

# Time Complexity
print("\nTime Complexity:")
print("Best Case   : O(1)")
print("Average Case: O(n)")
print("Worst Case  : O(n)")
print("Space Complexity: O(1)")
