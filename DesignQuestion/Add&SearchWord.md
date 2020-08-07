```text
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.
```

```go
package main
type WordDictionary struct {
    nodes []*WordDictionary
    isEnd bool
}

func (this *WordDictionary) put(char int32) {
    w := Constructor()
    this.nodes[char-97] = &w
}

func (this *WordDictionary) get(char int32) *WordDictionary{
    return this.nodes[char-97]
}

func (this *WordDictionary) setEnd() {
    this.isEnd = true
}

func (this *WordDictionary) IsEnd() bool{
    return this.isEnd
}

func (this *WordDictionary) containsKey(char int32) bool{
    return this.nodes[char-97] != nil
}

func (this *WordDictionary) searchPrefix(word string) bool{
    for index,c:=range word{
        if c!=46 && !this.containsKey(c){
            return false
        }
        if c!=46 && this.containsKey(c){
            if len(word)-1 ==index{
                fmt.Println(word,index,len(word)-1)
                return false
            }
        }
        if c==46{
            var i int32
            var n *WordDictionary
            for ;i<26;i++{
                n = this.get(i+97)
                if n!=nil{
                    if n.searchPrefix(word[index+1:]){
                        return true
                    }
                }
            }
        }else{
            this = this.get(c)
        }
    }
    return this != nil && this.IsEnd()
}

/** Initialize your data structure here. */
func Constructor() WordDictionary {
    w := WordDictionary{}
    w.nodes = make([]*WordDictionary,26,26)
    return w
}


/** Adds a word into the data structure. */
func (this *WordDictionary) AddWord(word string)  {
    for _,c:=range word{
        if !this.containsKey(c){
            this.put(c)
        }
        this = this.get(c)
    }
    this.setEnd()
}


/** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
func (this *WordDictionary) Search(word string) bool {
    return this.searchPrefix(word)
}


/**
 * Your WordDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddWord(word);
 * param_2 := obj.Search(word);
 */
```

```go
type WordDictionary struct {
    nodes []*WordDictionary
    isEnd bool
}


/** Initialize your data structure here. */
func Constructor() WordDictionary {
    w := WordDictionary{}
    w.nodes = make([]*WordDictionary,26)
    for i:=0;i<26;i++{
        w.nodes[i]=nil
    }
    return w
}


/** Adds a word into the data structure. */
func (this *WordDictionary) AddWord(word string)  {
    for _,c:=range word{
        if this.nodes[c-97]==nil{
            w := Constructor()
            this.nodes[c-97]=&w
        }
        this = this.nodes[c-97]
    }
    this.isEnd=true
}


/** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
func (this *WordDictionary) Search(word string) bool {
    for index,c:=range word{
        if byte(c)=='.'{
            for i:=0;i<26;i++{
                if this.nodes[i]!=nil{
                    temp := this.nodes[i]
                    if index < len(word)-1{
                        if temp.Search(word[index+1:]){
                            return true
                        }
                    }else{
                        return true
                    }
                }
            }
        }else if this.nodes[c-97]!=nil{
           this=this.nodes[c-97]
        }else{
            return false
        }
    }
    return this.isEnd
}


/**
 * Your WordDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddWord(word);
 * param_2 := obj.Search(word);
 */
```