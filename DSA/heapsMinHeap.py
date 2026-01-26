# Concept of the Day: Heaps (Min-Heap)
# Explanation: A Heap is a special Tree-based structure that satisfies the Heap Property:
# Min-Heap: The parent is always smaller than its children. The Root is the smallest number in the entire tree.
# Max-Heap: The parent is always larger.
# Why use it?
# If you constantly need to access the "Highest Priority" or "Lowest Cost" item (like in Dijkstra's algorithm or a Task Scheduler), Heaps do this in $O(1)$ time, while keeping the rest organized in O(\log N).

import heapq

# Python's heapq is a Min-Heap by default
tasks = []

# 1. Push items (Priority, Task Name)
heapq.heappush(tasks, (3, "Do laundry"))
heapq.heappush(tasks, (1, "Fix critical bug")) # Priority 1 (Highest)
heapq.heappush(tasks, (2, "Write report"))

print(f"Heap Structure: {tasks}")
# Note: It's not perfectly sorted, but index 0 is ALWAYS the smallest.

# 2. Pop items (Always returns smallest priority first)
first = heapq.heappop(tasks)
print(f"Doing: {first}") # (1, "Fix critical bug")

second = heapq.heappop(tasks)
print(f"Doing: {second}") # (2, "Write report")