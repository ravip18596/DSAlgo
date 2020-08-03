```text
There is one meeting room in a firm. There are N meetings in the form of (S[i], F[i]) where S[i] is start time of meeting i and F[i] is finish time of meeting i.
What is the maximum number of meetings that can be accommodated in the meeting room?

Example:
Input:
2
6
1 3 0 5 8 5
2 4 6 7 9 9
8
75250 50074 43659 8931 11273 27545 50879 77924
112960 114515 81825 93424 54316 35533 73383 160252  

Output:
1 2 4 5
6 7 1 
```

`Solution approach`

```text
Problem similar to the activity selection problem.
1) Sort the meeting according to their finishing time
2) Select the first meeting from the sorted array and print it.
3) Perform for remaining activities in the sorted array.
    a) If the start time of this meeting is greater than or equal to the finish time of previously selected activity then select this activity and print it.
```


`Solution`

```cpp
#include <bits/stdc++.h> 
using namespace std;

struct meeting { 
    int start; 
    int end; 
    int pos; 
}; 
bool compare(meeting room1,meeting room2) {
    return (room1.end < room2.end);
}
int main() {
	//code
	int t;
	cin>>t;
	while(t--){
	    int n;
	    cin>>n;
	    int *start = new int[n];
	    int *finish = new int[n];
	    for(int i=0;i<n;i++){
	        cin>>start[i];
	    }
	    for(int i=0;i<n;i++){
	        cin>>finish[i];
	    }
	    struct meeting meet[n];
	    for(int i=0;i<n;i++){
	        meet[i].start = start[i];
	        meet[i].end = finish[i];
	        meet[i].pos = i+1;
	    }
	    sort(meet,meet+n,compare);
	    cout<<meet[0].pos;
	    int lastFinishTime = meet[0].end;
	    for(int i=1;i<n;i++){
	        if(meet[i].start>lastFinishTime){
	            cout<<" "<<meet[i].pos;
	            lastFinishTime = meet[i].end;
	        }
	    }
	    cout<<endl;
	}
	return 0;
}
```