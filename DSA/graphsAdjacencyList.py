# Concept of the Day: Graphs (Adjacency List)
# Explanation: A Graph is a network of nodes (Vertices) connected by lines (Edges).
# Examples: Social Networks (You -> Friend), Maps (City -> Highway -> City).
# Adjacency List: The most common way to represent a graph in code.
# It's a Dictionary/HashMap where the Key is the Node, and the Value is a list of neighbors.


# Graph Representation
# A is connected to B and C
# B is connected to A and D
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

# Print all connections
print("--- Network Connections ---")
for node, neighbors in graph.items():
    print(f"{node} is connected to: {neighbors}")

# Check if A is connected to D
if "D" in graph["A"]:
    print("Direct connection exists.")
else:
    print("No direct connection.")