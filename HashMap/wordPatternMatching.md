# Problem

Given a dictionary of words, find all strings that match the given pattern where every character in the pattern is uniquely mapped to a character in the dictionary.

Examples:

Input:  
dict = ["abb", "abc", "xyz", "xyy"];
pattern = "foo"
Output: [xyy abb]
xyy and abb have same character at 
index 1 and 2 like the pattern

Input: 
dict = ["abb", "abc", "xyz", "xyy"];
pat = "mno"
Output: [abc xyz]
abc and xyz have all distinct characters,
similar to the pattern.

Input:  
dict = ["abb", "abc", "xyz", "xyy"];
pattern = "aba"
Output: [] 
Pattern has same character at index 0 and 2. 
No word in dictionary follows the pattern.

Input:  
dict = ["abab", "aba", "xyz", "xyx"];
pattern = "aba"
Output: [aba xyx]
aba and xyx have same character at 
index 0 and 2 like the pattern


# Solution
Approach: The aim is to find whether the word has the same structure as the pattern. An approach to this problem can be to make a hash of the word and pattern and compare if they are equal or not. In simple language, we assign different integers to the distinct characters of the word and make a string of integers (hash of the word) according to the occurrence of a particular character in that word and then compare it with the hash of the pattern.

Example:

Word='xxyzzaabcdd'
Pattern='mmnoopplfmm'
For word-:
map['x']=1;
map['y']=2;
map['z']=3;
map['a']=4;
map['b']=5;
map['c']=6;
map['d']=7;
Hash for Word="11233445677"

For Pattern-:
map['m']=1;
map['n']=2;
map['o']=3;
map['p']=4;
map['l']=5;
map['f']=6;
Hash for Pattern="11233445611"
Therefore in the given example Hash of word 
is not equal to Hash of pattern so this word 
is not included in the answer


```python
def findSpecificPattern(Dict, pattern):
    #Code here
    def encode(word):
        m = {}
        s = ""
        counter = 0
        for c in word:
            if c not in m:
                m[c] = counter
                counter += 1
            
            s += str(m[c])
        return s
            
    pattern_hash = encode(pattern)
    
    result = []
    for word in Dict:
        word_hash = encode(word)
        #print(word_hash, pattern_hash)
        if pattern_hash == word_hash:
            result.append(word)
            
    return result
```