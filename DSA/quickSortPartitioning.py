# Concept of the Day: Quick Sort (Partitioning)
#
# Explanation:Merge Sort (Day 26) splits the list in the middle.
#
# Quick Sort splits the list based on a Pivot.
#
# Pick a number (the Pivot).
#
# Move everything smaller to the left.
#
# Move everything larger to the right.
#
# Repeat for the left and right sides.
#
# Speed: Usually faster than Merge Sort in practice (O(N \log N)),
#
# but can be slow (O(N^2)) if you pick a bad pivot (like the smallest number).

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Pick middle element as pivot

    left = [x for x in arr if x < pivot]  # Smaller items
    middle = [x for x in arr if x == pivot]  # Equal items
    right = [x for x in arr if x > pivot]  # Larger items

    # Recursive magic
    return quick_sort(left) + middle + quick_sort(right)


print(quick_sort([3, 6, 8, 10, 1, 2, 1]))
# Output: [1, 1, 2, 3, 6, 8, 10]