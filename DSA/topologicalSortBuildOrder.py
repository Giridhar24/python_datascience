# Concept of the Day: Topological Sort (Build Order)
#
# Explanation: Imagine a university course system. You must take "Math 101" before "Calculus".
#
# You must take "Calculus" before "Physics".
#
# Topological Sort arranges these nodes in a straight line so that all prerequisites come before the dependent task.
#
# Constraint: The graph must be a DAG (Directed Acyclic Graph). You can't have a cycle (A requires B, B requires A).


from collections import deque, defaultdict


def topological_sort(num_courses, prerequisites):
    # 1. Build Graph and Count In-Degrees (Incoming edges)
    graph = defaultdict(list)
    in_degree = [0] * num_courses

    for course, pre in prerequisites:
        graph[pre].append(course)
        in_degree[course] += 1

    # 2. Add all courses with NO prerequisites to queue
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    order = []

    # 3. Process
    while queue:
        current = queue.popleft()
        order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == num_courses else []  # Empty if cycle detected


# 0: Intro, 1: Advanced, 2: Expert
# Prereqs: [1 needs 0], [2 needs 1]
print(topological_sort(3, [[1, 0], [2, 1]]))
# Output: [0, 1, 2] (Intro -> Advanced -> Expert)