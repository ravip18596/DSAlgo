# Trie

## Implement Trie (Prefix Tree)

[208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)

```python
class Trie:

    def __init__(self):
        self.is_end = False
        self.children = [None]*26
        

    def search_prefix(self, word: str):
        for c in word:
            if self.children[ord(c) - ord('a')] is not None:
                self = self.children[ord(c) - ord('a')]
            else:
                return None

        return self


    def insert(self, word: str) -> None:
        for c in word:
            if self.children[ord(c)-ord('a')] is None:
                self.children[ord(c)-ord('a')] = Trie()
            
            self = self.children[ord(c)-ord('a')]

        # set end as flag
        self.is_end = True

    def search(self, word: str) -> bool:
        node = self.search_prefix(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.search_prefix(prefix)
        return node is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```
