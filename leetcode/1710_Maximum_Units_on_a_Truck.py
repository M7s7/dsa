# You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
    # numberOfBoxesi is the number of boxes of type i.
    # numberOfUnitsPerBoxi is the number of units in each box of the type i.
# You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.
# Return the maximum total number of units that can be put on the truck.


# Reverse sort (according to box capacity). Start from highest capacity box and exhaust
    # Time Complexity: O(nlogn) for sorting (can also do bucket sort instead for O(N))
    # Space Complexity: O(N)
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse = True, key = lambda x: x[1])
        units = 0
        i = 0
        while truckSize > 0 and i < len(boxTypes):
            boxes = min(truckSize, boxTypes[i][0])
            truckSize -= boxes
            units += boxes * boxTypes[i][1]
            i += 1
        return units