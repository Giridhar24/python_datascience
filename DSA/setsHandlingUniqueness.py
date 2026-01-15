# Concept of the Day: Sets (Handling Uniqueness)
# Explanation:A Set is a collection of items that must be unique.
# If you try to add a duplicate, the Set ignores it.
# Key Operation: Checking if an item exists is $O(1)$ (Instant), unlike a List which is $O(N)$ (Slow).
# Venn Diagrams: Sets support mathematical operations like Union (Combine) and Intersection (Overlap).

# Creating sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# 1. Intersection (What is in BOTH?)
# Useful for: "Find customers who bought both Item A AND Item B"
overlap = set_a.intersection(set_b)
print(f"Intersection: {overlap}") # {3, 4}

# 2. Difference (What is in A but NOT in B?)
# Useful for: "Find customers who started checkout but didn't finish"
diff = set_a.difference(set_b)
print(f"Difference: {diff}") # {1, 2}

# 3. Removing Duplicates from a List
raw_list = [10, 10, 20, 20, 30]
unique_set = set(raw_list)
print(f"Unique: {unique_set}") # {10, 20, 30}