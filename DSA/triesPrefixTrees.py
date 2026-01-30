# Concept of the Day: Tries (Prefix Trees)
#
# Explanation:How do Google Autocomplete work so fast? If you type "Ca", it instantly suggests "Cat", "Car", "Cake".
#
# It uses a Trie (pronounced "Try"). It is a tree where each node is a letter.
#
# Efficiency: To find "Cat", you just follow C -> A -> T.
#
# It takes $O(L)$ where $L$ is the word length (e.g., 3 steps), regardless of whether you have 1 million words in the dictionary.

class TrieNode:
    def __init__(self):
        self.children = {} # Dictionary of letters
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

t = Trie()
t.insert("apple")
print(t.search("apple")) # True
print(t.search("app"))   # False (It's a prefix, but not a full word)