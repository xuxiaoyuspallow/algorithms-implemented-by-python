# coding:utf-8
"""
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
"""


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        neg = False
        res = []
        if num < 0:
            neg = True
            num = abs(num)
        while num :
            res.append(str(num % 7))
            num = num // 7
        if neg:
            res.append('-')
        res.reverse()
        return ''.join(res)
