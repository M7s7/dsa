# You are given an array that contains 1 to n elements. Your task is to sort this array in an efficient way.


def main():
    nums = [8,6,9,4,3,7,2,6,1]
    print(cyclic_sort(nums))

def cyclic_sort(nums):
    i = 0

    while i < len(nums):
        # J is the array number that i belongs to
        j = nums[i] - 1
        # Thus, we want to swap nums[i] with nums[j] if they aren't equal
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        
        # If the number is in the right place, go to the next
        else:
            i += 1
    return nums

main()