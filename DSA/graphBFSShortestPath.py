# Concept of the Day: Graph BFS (Shortest Path)
# Explanation: If you want to find the shortest path (fewest stops) between two nodes in an unweighted graph, use BFS.
# Logic: BFS checks all neighbors (distance 1) before moving to neighbors-of-neighbors (distance 2).
# Therefore, the first time you hit the target, you are guaranteed to have found the shortest route.

from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}


def bfs_shortest_path(start, target):
    queue = deque([(start, 0)])  # Store (Node, Distance)
    visited = set()

    while queue:
        current_node, dist = queue.popleft()

        if current_node == target:
            return dist

        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph[current_node]:
                queue.append((neighbor, dist + 1))
    return -1


print("Distance A to F:", bfs_shortest_path("A", "F"))
# Output: 2 (A -> C -> F)