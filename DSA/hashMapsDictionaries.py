# Concept of the Day: Hash Maps (Dictionaries)
# Explanation:Yesterday we learned Arrays are fast at reading ($O(1)$) but slow at searching ($O(N)$).
# Hash Maps (called Dictionaries in Python, Objects in JS, HashMaps in Java) are the "Magic" data structure.
# They allow you to find data in $O(1)$ Constant Time using a "Key".
# Analogy: Instead of searching every page of a book for a definition (Array), you use the Index at the back to jump straight to the page (Hash Map).

# Creating a Hash Map
phone_book = {
    "Alice": "555-1234",
    "Bob": "555-9876"
}

# Lookup is O(1) - Instant
# It doesn't loop through the data; it jumps straight to "Alice"
print(phone_book["Alice"])