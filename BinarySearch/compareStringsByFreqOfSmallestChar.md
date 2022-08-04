```python
class Solution:
    def binary_search(self, arr, val):
        s, e = 0, len(arr)-1
        leftg = len(arr)
        while s<=e:
            mid = (s+e)//2
            if arr[mid]>val:
                leftg = mid
                e = mid-1
            else:
                s = mid+1
            
        return len(arr)-leftg
    
    def util(self, word):
        chars = 'abcdefghijklmnopqrstuvwxyz'
        freq = {}
        for c in chars:
            freq[c] = 0
        for c in word.lower():
            freq[c] += 1

        for c in chars:
            if freq[c] > 0:
                return freq[c]
            
        return 0
        
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        cnt_arr = []
        for word in words:
            cnt_arr.append(self.util(word))
                
        cnt_arr = sorted(cnt_arr)
        return [self.binary_search(cnt_arr, self.util(q)) for q in queries]
```
