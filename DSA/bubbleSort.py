# Concept of the Day: Bubble Sort
# Explanation: Bubble Sort is a simple (but slow) sorting algorithm. Logic:
# Compare two adjacent numbers.
# If they are in the wrong order (Left > Right), swap them.
# Repeat this process until the largest number "bubbles" to the top (end of the list).
# Do it again for the remaining numbers.

def bubble_sort(arr):
    n = len(arr)

    # Loop through all elements
    for i in range(n):
        # Last i elements are already in place, so ignore them
        for j in range(0, n - i - 1):

            # Check if current element is greater than the next
            if arr[j] > arr[j + 1]:
                # SWAP
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"Sorted: {bubble_sort(numbers)}")