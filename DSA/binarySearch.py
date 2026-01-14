# Concept of the Day: Binary Search
# Explanation:Yesterday's "Bubble Sort" helped us sort data.
# Why sort? Because Binary Search only works on sorted lists, and it is incredibly fast ($O(\log N)$).
# Instead of checking items one by one (Linear Search), Binary Search checks the middle.
# Is the middle number too high? Cut the right half of the list.
# Is it too low? Cut the left half.
# Repeat.

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Find the middle index

        if arr[mid] == target:
            return mid  # Found it! Return index.
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half

    return -1  # Not found


# List MUST be sorted
sorted_list = [10, 20, 30, 40, 50, 60, 70]
index = binary_search(sorted_list, 50)
print(f"Number 50 found at index: {index}")