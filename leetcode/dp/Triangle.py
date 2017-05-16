"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""


class Solution(object):
    # O(n*n/2) space, top-down
    def minimumTotal1(self, triangle):
        if not triangle:
            return
        res = [[0 for i in xrange(len(row))] for row in triangle]
        res[0][0] = triangle[0][0]
        for i in xrange(1, len(triangle)):
            for j in xrange(len(triangle[i])):
                if j == 0:
                    res[i][j] = res[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    res[i][j] = res[i - 1][j - 1] + triangle[i][j]
                else:
                    res[i][j] = min(res[i - 1][j - 1], res[i - 1][j]) + triangle[i][j]
        return min(res[-1])

    # Modify the original triangle, top-down
    def minimumTotal2(self, triangle):
        if not triangle:
            return
        for i in xrange(1, len(triangle)):
            for j in xrange(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == len(triangle[i])-1:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[-1])

    # Modify the original triangle, bottom-up
    def minimumTotal3(self, triangle):
        if not triangle:
            return
        for i in xrange(len(triangle)-2, -1, -1):
            for j in xrange(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

    # bottom-up, O(n) space
    def minimumTotal(self, triangle):
        if not triangle:
            return
        res = triangle[-1]
        for i in xrange(len(triangle)-2, -1, -1):
            for j in xrange(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        return res[0]
