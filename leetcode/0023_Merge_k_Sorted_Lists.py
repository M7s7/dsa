# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Priority queue to store each list's head node and its value
# When smallest element is found, push it onto our answers and go to the next node of that list

# My original implementation. Since nodes cannot act as tie-breakers in heaps(it breaks the heap), we store the list index of the node instead.
    # Time Complexity: O(NlogK), where N is the total number of nodes, and k is the number of lists. 
    # Space Complexity: O(k)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ans = ListNode(None)
        min_heap = []
        # Initialise our heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i))
            
        while min_heap:
            val, i = heapq.heappop(min_heap)
            ans.next = lists[i]
            ans = ans.next
            # Check if there are any new nodes to put back on
            if lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(min_heap, (lists[i].val, i))
        
        return head.next


# This solution stores the actual node as well in the heap. The tuples are triplets instead of ordered pairs. 
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ans = ListNode(None)
        min_heap = []
        # Initialise our heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
            
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            ans.next = node
            ans = ans.next
            # Check if there are any new nodes to put back on
            if node.next:
                node = node.next
                heapq.heappush(min_heap, (node.val, i, node))
        
        return head.next