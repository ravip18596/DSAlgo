# Problem

The LRUCache class has two methods get() and set() which are defined as follows.

- get(key)   : returns the value of the key if it already exists in the cache otherwise returns -1.
- set(key, value) : if the key is already present, update its value. If not present, add the key-value pair to the cache. If the cache reaches its capacity it should invalidate the least recently used item before inserting the new item.

# Solution

```python
class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self,cap):
        #code here
        self.cap = cap
        self.cache = {}
        self.freq = {}
        self.timer = 1
        
        
    #Function to return value corresponding to the key.
    def get(self, key):
        #code here
        if key in self.cache:
            self.freq[key]=self.timer
            self.timer+=1
            return self.cache[key]
        else:
            return -1
        
    #Function for storing key-value pair.   
    def set(self, key, value):
        #code here
        if key in self.cache:
            self.cache[key] = value
            
        elif self.cap>0:
            self.cap-=1
            self.cache[key] = value
        else:
            minKey, mint = 0,int(1e9+7)
            for k, t in self.freq.items():
                if t < mint:
                    mint = t
                    minKey = k
            
            del self.cache[minKey]
            del self.freq[minKey]
            
            self.cache[key] = value
        
        self.freq[key]=self.timer
        self.timer+=1
```

- Approach 2

Double Linked List

```python
class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=self.pre=None

class LRUCache:
    #Constructor for initializing the cache capacity with the given value.
    def __init__(self,cap):
        self.hsmap=dict()
        self.capacity=cap
        self.head=Node(0,0)
        self.tail=Node(0,0)
        
        self.head.next=self.tail
        self.head.pre=None
        self.tail.next=None
        self.tail.pre=self.head
        self.count=0
        
    def addToHead(self,node):
        node.next=self.head.next
        node.next.pre=node
        node.pre=self.head
        self.head.next=node
    
    #Function to delete a node.
    def deleteNode(self,node):
        node.pre.next=node.next
        node.next.pre=node.pre
    
    #Function to return value corresponding to the key.
    def get(self,key):
        
        #if element is present in map,
        if key in self.hsmap:
            
            node=self.hsmap[key]
            result=node.value
            self.deleteNode(node)
            self.addToHead(node)
            
            #returning the value.
            return result
         
        #else we return -1.   
        else:
            return -1
        
    #Function for storing key-value pair.   
    def set(self,key,value):
        
        if key in self.hsmap:
            
            node=self.hsmap[key]
            node.value=value
            self.deleteNode(node)
            self.addToHead(node)
        else:
            node=Node(key,value)
            self.hsmap[key]=node
            
            if self.count<self.capacity:
                self.count+=1
                self.addToHead(node)
            else:
                self.hsmap.pop(self.tail.pre.key)
                self.deleteNode(self.tail.pre)
                self.addToHead(node)
```