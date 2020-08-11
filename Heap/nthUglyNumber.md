```text
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
```
`Heap Solution Time - NlogN (N heap inserts) Space-O(N)`

```cgo
typedef long long ll;
int nthUglyNumber(int n) {
    //min heap - priority_queue <int, vector<int>, greater<int>> 
    priority_queue<ll, vector<ll>, greater<ll>> minheap;
    minheap.push(1);
    for(int i=1;i<n;i++){
        ll top = minheap.top();
        //duplicate handling
        while(!minheap.empty() && top==minheap.top()){
            minheap.pop();
        }
        minheap.push(top*2);
        minheap.push(top*3);
        minheap.push(top*5);
    }
    return minheap.top();
}
```

`DP solution Time-O(N)`

```textmate
Let's say we have the first 3 ugly numbers 1, 2, 3.
What would be the next number? Given the definition,
the next number has to be the the smallest number among 2*(1,2,3), 3*(1,2,3), 5*(1,2,3).
Obviously, the smallest number is 2 * 1 = 2. But wait, 2 is already in there.
So precisely speaking, the next number has to be the the smallest number among all the existing numbers multiplied by 2,3,5
that isn't in the list already. Now, we can traverse all numbers and maintain a hashset if we want, but it would become O(N^2).
Good news is that we can solve this in a DP-like approach. First, we assume there is only one number in the list, which is 1.
The next number is Min(2 * 1, 3 * 1, 5 * 1)=2 and it is not in the list. 
Because we have already considered 2*1 (we move the pointer to its next position, which is 2), now we only need to consider 2 * 2, 3 * 1, 5 * 1 in the next iteration. 
This way, we don't have to worry about finding a number that is already in the list.
```
```go
package main
func nthUglyNumber(n int) int {
    if n<=0 { return 0 }
    if n==1 { return 1 }
    //
    k2,k3,k5 := 0,0,0 //
    ugly := []int{1}
    for i:=1;i<n;i++{
        ithUglyNo := min(ugly[k2]*2,min(ugly[k3]*3,ugly[k5]*5))
        ugly = append(ugly,ithUglyNo)
        if ithUglyNo%2==0 { k2++ }
        if ithUglyNo%3==0 { k3++ }
        if ithUglyNo%5==0 { k5++ }
    }
    return ugly[n-1]
}

func min(a,b int) int{
    if a<b{
        return a
    }
    return b
}
```