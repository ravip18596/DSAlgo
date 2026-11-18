"""
Leetcode 621

You are given an array of CPU `tasks`, each represented by a single uppercase English letter
from 'A' to 'Z', and a non-negative integer `n` representing the cooldown interval between
two identical tasks.

Each interval, the CPU can either execute one task or remain idle. However, there must be
at least `n` intervals between two executions of the same task.

Return the minimum number of intervals the CPU will take to finish all the given tasks.

Constraints:
- 1 <= len(tasks) <= 10^4
- tasks[i] is an uppercase English letter ('A' - 'Z')
- 0 <= n <= 100
"""
from typing import List
from collections import Counter
import heapq

def leastInterval(tasks: List[str], n: int) -> int:
    max_heap = []
    c = Counter(tasks)
    for task, freq in c.items():
        heapq.heappush(max_heap, (-freq, task))

    ans = 0
    while max_heap:
        i = 0
        task_list = set()
        while i<n+1:
            if len(max_heap) == 0:
                break
            freq, task = heapq.heappop(max_heap)
            freq *= -1

            if freq >= 1:
                ans += 1
                print(f"{task}->", end='')
                freq -= 1
                if freq > 0:
                    task_list.add((freq, task))
            i+=1

        for freq, task in task_list:
            heapq.heappush(max_heap, (-freq, task))

        if len(max_heap) > 0:
            # adding count for idle
            print("idle->", end='')
            ans += (n+1) - i

    return ans

if __name__ == '__main__':
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print()
    print(leastInterval(tasks, n))

    tasks = ["A", "C", "A", "B", "D", "B"]
    n = 1
    print()
    print(leastInterval(tasks, n))

    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 3
    print()
    print(leastInterval(tasks, n))

    '''
    Space complexity is O(K) where K is len of tasks which is 26 so, ~O(1)
    Time complexity is O(NlogK) where K is len of tasks which is 26 so, ~O(N)
    '''