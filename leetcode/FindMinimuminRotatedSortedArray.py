"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

Subscribe to see which companies asked this question
"""


class Solution(object):
    """this is not a right way to write an algorithm exam,but whatever..."""
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[0]
