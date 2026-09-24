class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest =-1
        second_largest =-1
        largest_index =-1
        for i in range(len(nums)):
            if nums[i]>largest:
                second_largest = largest
                largest = nums[i]
                largest_index = i
            elif nums[i]>second_largest:
                second_largest =nums[i]
        if largest >= 2 * second_largest:
            return largest_index
        return -1
        