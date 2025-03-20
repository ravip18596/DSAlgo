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

    def print_words_from_node(self, root, res, prefix=''):
        if root.is_end:
            res.append(prefix)
        
        for i,child_node in enumerate(root.children):
            if child_node:
              self.print_words_from_node(child_node, res, prefix + chr(ord('a')+i))

          
    def auto_complete(self, w, root) -> List[str]:
        #Write your code here
        # w is the prefix here
        for c in w:
            if root.children[ord(c)-ord('a')] is None:
              return -1
            root = root.children[ord(c)-ord('a')]
    
        res = []
        if root is None:
            return res
        
        self.print_words_from_node(root, res, w)
        return res


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```
