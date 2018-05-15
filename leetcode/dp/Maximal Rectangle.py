"""

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not any(matrix):
            return 0
        height = [0] * (len(matrix[0]) + 1)
        ans = 0
        for row in matrix:
            for j in range(len(row)):
                height[j] = height[j] + 1 if row[j] == '1' else 0
            stack = [-1]
            for i in range(len(row) + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - stack[-1] -1
                    ans = max(ans, h*w)
                stack.append(i)
        return ans


