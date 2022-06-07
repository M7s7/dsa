# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array, nums1, sorted in non-decreasing order.
# Note that nums1 will have trailing zeroes to accomodate the numbers from nums2. 


# Approach: Since both lists are sorted, we can compare the back numbers to see which one is larger. We can sort the arrays backwards, placing the larger number at the back of the final array. 
    # We will keep going through the lists until one is exhausted (eg. we are in the -1 index of one of the lists).
        # If we have exhausted nums2, that is fine as it implies that the rest of our nums1 is already in order. 
        # If we have exhausted nums1, it means that we have placed all the numbers from nums1 to the right of the last_index pointer. Thus, the remaining numbers will be all from nums2. 
            # Therefore, we will go through nums2 and insert the numbers backwards into nums1. 
    # Time Complexity: O(N + M) as we iterate through both lists
    # Space Complexity: O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initiate pointers
        last_index = len(nums1) - 1 # Insert largest numbers at this index
        m_index = m - 1 # Largest number of nums1
        n_index = n - 1 # Largest number of nums2
        
        # Compare largest numbers until one array has no more numbers (index is at -1)
        while m_index >= 0 and n_index >= 0:
            m_value = nums1[m_index]
            n_value = nums2[n_index]
            
            if m_value > n_value:
                nums1[last_index] = m_value
                m_index -= 1
            
            else:
                nums1[last_index] = n_value
                n_index -= 1
                
            last_index -= 1
        
        # If nums1 is exhausted but not nums2, the left of nums2 pointer must have the smallest numbers. Insert them into nums1
        while n_index >= 0:
            n_value = nums2[n_index]
            nums1[last_index] = n_value
            n_index -= 1
            last_index -= 1 
        # If nums2 is exhausted, then the left of nums1 must have the smallest numbers. Thus, we don't need to do anything as it is already sorted. 
        return nums1