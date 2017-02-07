"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==1 or n== 2:
            return n
        one_step_before = 2
        two_steps_before = 1
        all_ways = 0
        for i in range(2,n):
            all_ways = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = all_ways
        return all_ways

if __name__ == '__main__':
    s = Solution()
    s.climbStairs(4)