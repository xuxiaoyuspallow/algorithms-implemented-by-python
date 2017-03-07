"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        local_min = nums[0]
        local_max= nums[0]
        global_max = nums[0]
        for i in range(1,len(nums)):
            local_max_copy = local_max
            local_max = max(max(local_max*nums[i],nums[i]),local_min*nums[i])
            local_min = min(min(nums[i]*local_max_copy,nums[i]),nums[i]*local_min)
            global_max = max(global_max,local_max)
        return global_max
