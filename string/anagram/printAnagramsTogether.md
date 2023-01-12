# Problem

Given an array of strings, return all groups of strings that are anagrams. The groups must be created in order of their appearance in the original array

Input:
N = 5
words[] = {act,god,cat,dog,tac}
Output:
act cat tac 
god dog

Input:
N = 3
words[] = {no,on,is}
Output: 
is
no on

# Solution

```python
class WordIndex:
    def __init__(self, data, index):
        self.data = data
        self.index = index
        
class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        #code here
        wordIndexArr = []
        for i in range(n):
            sortedWord = ''.join(sorted(words[i]))
            wordIndexArr.append(WordIndex(data=sortedWord, index=i))
            
        wordIndexArr = sorted(wordIndexArr, key=lambda x: x.data)
        groups = []
        group = [words[wordIndexArr[0].index]]
        for i in range(1,n):
            if wordIndexArr[i-1].data != wordIndexArr[i].data:
                groups.append(group)
                group = []
               
            group.append(words[wordIndexArr[i].index])
            
        if len(group) > 0:
            groups.append(group)
        
        return groups
```