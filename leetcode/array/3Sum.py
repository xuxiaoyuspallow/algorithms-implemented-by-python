class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l,h = i + 1, len(nums) - 1
            while l < h :
                if nums[i] + nums[l] + nums[h] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[h] > 0:
                    h -= 1
                else:
                    res.append([nums[i],nums[l],nums[h]])
                    while l < h and nums[l] == nums[l+ 1]:
                        l += 1
                    while l < h and nums[h] == nums[h - 1]:
                        h -= 1
                    l += 1
                    h -= 1
        return res
