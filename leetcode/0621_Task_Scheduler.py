

# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. 
# Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
# Return the least number of units of times that the CPU will take to finish all the given tasks.

import heapq
import collections

# Approach: Max heap to access most frequent tasks (char doesnt matter). Then, keep a queue of used elements. 
    # We can store the tasks as TUPLES in the queue, with one of values as the time when it can be used again and the other as frequency. 
    # We can end the loop when we have completed all tasks (no queue or heap left).
        # Time Complexity: O(N * k), where N is the amount of tasks, and k is the waiting time
        # Space Complexity: O(N).
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if len(tasks) < 2:
            return len(tasks)
        
        total_time = 0
        freq = collections.Counter(tasks)
        max_heap = [-val for val in freq.values()]
        heapq.heapify(max_heap)
        next_task = collections.deque()
        
        while max_heap or next_task:
            total_time += 1
            if max_heap:
                val = heapq.heappop(max_heap) + 1
                if val != 0:
                    next_task.append((val, total_time + n))
    
            if next_task and next_task[0][1] == total_time:
                new_task = next_task.popleft()
                heapq.heappush(max_heap, new_task[0])
                
        return total_time


# My implementation of the above approach. Space complexity gets super large because we add the idles. 
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if len(tasks) < 2:
            return len(tasks)
        
        total_time = 0
        tasks_left = len(tasks)
        freq = collections.Counter(tasks)
        max_heap = [-val for val in freq.values()]
        heapq.heapify(max_heap)
        next_task = collections.deque()
        
        while tasks_left > 0:
            total_time += 1
            if max_heap:
                val = heapq.heappop(max_heap)
                val += 1
                tasks_left -= 1
                if val != 0:
                    next_task.append((val, total_time + n))
    
            if next_task and next_task[0][1] <= total_time:
                new_task = next_task.popleft()
                heapq.heappush(max_heap, new_task[0])
                
        return total_time