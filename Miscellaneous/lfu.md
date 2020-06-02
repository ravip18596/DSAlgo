Least Frequently used cache

`Solution`

```go
package main
import "time"

type Cache struct{
    key,value int
    lastUsedTime int64
    freq int
}

type LFUCache struct {
    data []*Cache
    capacity int
    m map[int]int
}


func Constructor(capacity int) LFUCache {
    c := LFUCache{}
    c.data = make([]*Cache,0)
    c.capacity = capacity
    c.m = make(map[int]int)
    return c
}


func (this *LFUCache) Get(key int) int {
    value := -1
    if v,ok:=this.m[key];ok && v!=-1{
        value = this.data[v-1].value
        this.data[v-1].freq = this.data[v-1].freq + 1
        this.data[v-1].lastUsedTime = time.Now().UnixNano()
    }
    return value
}


func (this *LFUCache) Put(key int, value int)  {
    c := Cache{
        key:key,
        value:value,
        freq:1,
        lastUsedTime:time.Now().UnixNano(),
    }
    if this.capacity==0{
        this.m[key]=-1
        return
    }
    if v,ok:=this.m[key];ok && v!=-1{
        this.data[v-1].value = value
        this.data[v-1].freq = this.data[v-1].freq + 1
        this.data[v-1].lastUsedTime = time.Now().UnixNano()
    }else if len(this.data)==this.capacity{
        mini := 2147483647
        minT := time.Now().UnixNano()
        var index int
        for i:=0;i<len(this.data);i++{
            if mini > this.data[i].freq{
                mini=this.data[i].freq
                minT = this.data[i].lastUsedTime
                index=i
            }else if mini==this.data[i].freq && minT > this.data[i].lastUsedTime{
                index = i
                minT = this.data[i].lastUsedTime
            }
        }
        //fmt.Println(index)
        this.m[this.data[index].key] = -1
        this.data[index] = &c
        this.m[key] = index+1
    }else{
        this.data = append(this.data,&c)
        this.m[key] = len(this.data)
    }
}

```

