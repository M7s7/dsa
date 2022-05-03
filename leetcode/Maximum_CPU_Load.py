from heapq import *

#class job:
    #def __init__(self, start, end, cpu_load):
    #    self.start = start
    #    self.end = end
    #    self.cpu_load = cpu_load

# Note: The job list could also be implemented as a 2D array 



# METHOD 1: Heap + hashmap. Heap only stores the END VALUES of intervals. 
# We sort the array of jobs by start times. We iterate through the intervals, and add their ends to the heap. Importantly, we also store the cpu_load value in the hashmap (usage[end_time] = cpu_load) for each end time. 
# Then, we check to see if the start time occurs after end times of the previous intervals. If it is, we pop off the cpu_usage and remove the corresponding cpu load from the running CPU. 

def find_max_cpu_load(jobs):
    # Sort jobs by start time
    jobs.sort(key = lambda x: x[0])
    # CPU is point-in-time CPU usage, max is the maximum so far
    CPU, max_CPU = 0, 0
    # Store usage for every interval, key = end, value = cpu_load
    usage = {}
    # Create a heap to hold end times of intervals, popping off minimums
    heap = []

    for i in range(len(jobs)):
        start = jobs[i][0]
        end = jobs[i][1]
        use = jobs[i][2]

        # Add time usage to records
        heappush(heap, end)
        CPU += use

        # If the end value is already in the dictionary, add the two cpu_loads together. Otherwise, create one
        if end in usage:
            usage[end] += use
        else: usage[end] = use

        # Check any overlapping intervals have been passed. If so, remove them from the cpu count and heap
        while start > heap[0]:
            CPU -= usage[heap[0]]
            heappop(heap)
        
        max_CPU = max(max_CPU, CPU)
    return max_CPU

def main():
    jobs = [[1,4,2], [2,4,1], [6,6,5]]
    print(find_max_cpu_load(jobs))

main()


# METHOD 2: Heap only, but the heap stores the ENTIRE INTERVAL (but still sorts by end value)
    # Taken from GeeksforGeeks 
class job:
 
    # Constructor of the Job
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load
 
    # lt means 'less than' - thus, this function defines that a class object is sorted as 'less than' by its end values. 
    def __lt__(self, other): #<------------ THIS PART IS ADDED, AND IS NECESSARY. IT ALLOWS US TO SORT THE HEAP BY END VALUES 
        # min heap based on job.end
        return self.end < other.end

def find_max_cpu_load(jobs):
    job.sort(key = lambda x: x.start)
    max_cpu_load, current_cpu_load = 0, 0
 
    # Min-Heap
    min_heap = []
 
    # Loop to iterate over the list
    # of the jobs given for the CPU
    for j in jobs:
 
        # Remove all the jobs from
        # the min-heap which ended
        while(len(min_heap) > 0 and
              j.start >= min_heap[0].end):
            current_cpu_load -= min_heap[0].cpu_load
            heappop(min_heap)
 
        # Add the current job
        # into min_heap
        heappush(min_heap, j)
        current_cpu_load += j.cpu_load
        max_cpu_load = max(max_cpu_load, current_cpu_load)
    return max_cpu_load
