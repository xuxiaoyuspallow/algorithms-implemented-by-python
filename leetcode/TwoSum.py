"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    # def twoSum(self, nums, target):
    #     """
    #     O(n^2) my solution
    #     """
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     for i,x1 in enumerate(nums):
    #         for j,x2 in enumerate(nums):
    #             if x1 + x2 == target and i != j:
    #                 return [i ,j]

    def twoSum(self,nums,target):
        """
        O(n) also my solution
        """
        buff_dict = {}
        for i, n in enumerate(nums):
            if target - n in buff_dict:
                return [buff_dict[target - n], i]
            else:
                buff_dict[n] = i
