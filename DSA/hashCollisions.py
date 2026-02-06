# Concept of the Day: Hash Collisions
#
# Explanation: A Hash Map maps a Key ("Alice") to an Index (5). What if "Bob" also hashes to Index 5? This is a Collision. We need a strategy to handle this:
#
# Chaining (Most Common): Index 5 doesn't hold just one item; it holds a Linked List. If Alice and Bob collide, we just add Bob to the list at Index 5.
#
# Open Addressing: If Index 5 is taken, try Index 6. If taken, try 7.

# A simple Hash Table using Chaining
hash_table = [[] for _ in range(10)] # 10 buckets

def insert(key, value):
    # Simple hash: length of string % 10
    index = len(key) % 10
    hash_table[index].append((key, value))

insert("apple", 1)  # len 5 -> index 5
insert("berry", 2)  # len 5 -> index 5 (COLLISION!)
insert("date", 3)   # len 4 -> index 4

print(hash_table)
# Output:
# Index 4: [('date', 3)]
# Index 5: [('apple', 1), ('berry', 2)]  <-- The Chain