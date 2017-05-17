"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10^n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])
"""
from functools import reduce


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        res = {}
        res[1] = 10
        multipy_str = [9,9,8,7,6,5,4,3,2]
        for i in range(2,n+1):
            res[i] = reduce(lambda x,y: x*y,multipy_str[:i]) + res[i-1]
            if i > 9:
                return res[9]
        return res[n]
