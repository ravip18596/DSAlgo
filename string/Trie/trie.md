 Implement a trie with insert, search, and startsWith methods.
 
 ```go
package main
type Trie struct {
    IsEnd bool
    Nodes []*Trie
}

func (this *Trie) containsKey(char int32) bool{
    return this.Nodes[char-97] != nil 
}

func (this *Trie) putKey(char int32,node *Trie){
    this.Nodes[char-97] = node 
}

func (this *Trie) get(char int32) *Trie{
    return this.Nodes[char-97] 
}

func (this *Trie) setEnd() {
    this.IsEnd = true
}

func (this *Trie) isEnd() bool{
    return this.IsEnd
}

func (this *Trie) searchPrefix(word string) *Trie{
    for _,c:=range word{
        if this.containsKey(c){
            this = this.get(c)
        }else{
            return nil
        }
    }
    return this
}

/** Initialize your data structure here. */
func Constructor() Trie {
    t := Trie{}
    t.Nodes = make([]*Trie,26,26)
    for i:=0;i<26;i++{
        t.Nodes[i] = nil
    }
    return t
}


/** Inserts a word into the trie. */
func (this *Trie) Insert(word string)  {
    //Worst case complexity - O(m*n)
    for _,c:=range word{
        if !this.containsKey(c){
            t := Constructor()
            this.putKey(c,&t)
        }
        this = this.get(c)
    }
    this.setEnd()
}


/** Returns if the word is in the trie. */
func (this *Trie) Search(word string) bool {
    t := this.searchPrefix(word)
    return t!=nil && t.isEnd()
}


/** Returns if there is any word in the trie that starts with the given prefix. */
func (this *Trie) StartsWith(prefix string) bool {
    t := this.searchPrefix(prefix)
    return t!=nil
}


/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
```