"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
            return 0
        str_x = str(x)
        flag = False
        if not str_x.startswith('-'):
            flag = True
        result = str_x[::-1]
        result = result.strip('0')
        if not flag:
            result = result.rstrip('-')
            result = '-' + result
        if abs(int(result)) >= 2 ** 31:
            return 0
        return int(result)
