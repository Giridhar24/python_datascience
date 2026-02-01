# Concept of the Day: Merge Sort (Divide and Conquer)
#
# Explanation:Bubble Sort (O(N^2)) is too slow for big data.
#
# Merge Sort (O(N \log N)) is much faster.
#
# Divide: Cut the list in half recursively until every sub-list has only 1 item.
#
# Conquer (Merge): Merge the small lists back together in sorted order.

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive Split
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge Logic
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check for remaining items
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

data = [38, 27, 43, 3, 9, 82, 10]
merge_sort(data)
print(f"Sorted: {data}")