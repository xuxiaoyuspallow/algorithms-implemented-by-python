"""
39
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        res = []
        candidates = list(set(candidates))
        candidates.sort()
        self.backtrack([], res,candidates, target,0)
        return res

    def backtrack(self, temp, res,candidates, target,start):
        if sum(temp) > target:
            return
        if sum(temp) == target:
            res.append(temp)
            return
        for i in range(start,len(candidates)):
            self.backtrack(temp+[candidates[i]], res,candidates, target,i)

Solution().combinationSum([2,3,5],8)