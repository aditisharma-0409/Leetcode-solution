class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res =[]
        total = 0
        for num in nums:
            total += num
            res.append(total)
        return res
        