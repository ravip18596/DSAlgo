```text
Given an array A of size N having distinct elements, the task is to find the next greater element for each element of the array in order of their appearance in the array. If no such element exists, output -1 

Input:
The first line of input contains a single integer T denoting the number of test cases.Then T test cases follow. Each test case consists of two lines. The first line contains an integer N denoting the size of the array. The Second line of each test case contains N space separated positive integers denoting the values/elements in the array A.

Output:
For each test case, print in a new line, the next greater element for each array element separated by space in order.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1018
Example:
Input
2
4
1 3 2 4
4
4 3 2 1
Output
3 4 4 -1
-1 -1 -1 -1

Explanation:
Testcase1: In the array, the next larger element to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ? since it doesn't exist hence -1.
```

`Logic`
```text
Suppose we have a decreasing sequence followed by a greater number
For example [5, 4, 3, 2, 1, 6] then the greater number 6 is the next greater element for all previous numbers in the sequence

We use a stack to keep a decreasing sub-sequence, whenever we see a number x greater than stack.peek() we pop all elements less than x and for all the popped ones, their next greater element is x
For example [9, 8, 7, 3, 2, 1, 6]
The stack will first contain [9, 8, 7, 3, 2, 1] and then we see 6 which is greater than 1 so we pop 1 2 3 whose next greater element should be 6
```

```cgo
#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;

ll* nextGreaterElement(ll *arr,int n) {
    stack<ll> s;
    unordered_map<ll,ll> umap;
    s.push(arr[0]);
    for(int i=1;i<n;i++){
        //if stack is not a decreasing subsequence
        while(!s.empty() && arr[i] > s.top() ){
            //then pop and popped elements next greater ele is arr[i]
            umap[s.top()] = arr[i];
            s.pop();
        }
        s.push(arr[i]);
    }
    while(!s.empty()){
        umap[s.top()]=-1;
        s.pop();
    }
    ll *res = new ll[n];
    for(int i=0;i<n;i++){
        res[i] = umap[arr[i]];
    }
    return res;
}

int main() {
	//code
	int t;
	cin>>t;
	while(t--){
	    int n;
	    cin>>n;
	    ll *arr = new ll[n];
	    for(int i=0;i<n;i++){
	        cin>>arr[i];
	    }
	    ll *res;
	    res = nextGreaterElement(arr,n);
	    for(int i=0;i<n;i++){
	        if(i<n-1){
	            cout<<res[i]<<" ";
	        }else{
	            cout<<res[i]<<"\n";
	        }
	    }
	}
	return 0;
}
```


```go
package main
func nextGreaterElement(nums1 []int, nums2 []int) []int {
    if len(nums2)==0{
        return []int{}
    }
    stack := make([]int,0)
    m := make(map[int]int)
    stack = append(stack,nums2[0])
    for i:=1;i<len(nums2);i++{
        for len(stack)>0 && nums2[i] > stack[0]{
            m[stack[0]]=nums2[i];
            stack = stack[1:]
        }
        stack = append([]int{nums2[i]},stack...)
    }
    //those left behind in stack does not have next greater element
    for len(stack)>0{
        m[stack[0]] = -1
        stack=stack[1:]
    }
    for i:=0;i<len(nums1);i++{
        nums1[i] = m[nums1[i]];
    }
    return nums1
}
```