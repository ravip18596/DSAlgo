```python
class Solution:
    def partitionString(self, s: str) -> int:
        ch_map = [False]*26
        sub_str_cnt = 0
        
        for i, c in enumerate(s):
            if ch_map[ord(c)-ord('a')]:
                ch_map = [False]*26
                sub_str_cnt += 1
            
            ch_map[ord(c)-ord('a')] = True
            
        if ch_map[ord(c)-ord('a')]:
            sub_str_cnt += 1
            
        return sub_str_cnt
```
