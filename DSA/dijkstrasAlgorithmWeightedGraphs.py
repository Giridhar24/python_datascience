# Concept of the Day: Dijkstra’s Algorithm (Weighted Graphs)
# Explanation: BFS (Day 18) finds the shortest path by "number of stops."
# But in real life, roads have different lengths (Weights).
# A path with 3 short roads might be faster than 1 long road.
# Dijkstra's Algorithm uses a Priority Queue to always explore the cheapest known path first.

import heapq

# Graph: Node -> [(Neighbor, Cost), ...]
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}


def dijkstra(start, end):
    # Priority Queue stores (Cost, Node)
    # Automatically sorts so lowest cost is always popped first
    queue = [(0, start)]
    visited = set()

    while queue:
        cost, node = heapq.heappop(queue)

        if node == end:
            return cost

        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node]:
                heapq.heappush(queue, (cost + weight, neighbor))

    return float("inf")


print("Cost A to D:", dijkstra('A', 'D'))
# Output: 4 (Path: A -> B -> C -> D = 1 + 2 + 1)
# Direct BFS might have chosen A->B->D (Cost 6) or A->C->D (Cost 5)