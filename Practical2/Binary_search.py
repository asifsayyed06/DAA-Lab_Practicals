import time

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


# User input
n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter elements in sorted order: ").split()))

target = int(input("Enter element to search: "))

# Start execution time
start_time = time.perf_counter()

result = binary_search(arr, target)

# End execution time
end_time = time.perf_counter()

# Result
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")

# Execution time
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
