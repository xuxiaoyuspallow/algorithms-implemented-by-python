class Solution(object):
    def singleNonDuplicate(self, nums):
        l, h = 0, len(nums) - 1
        while l < h:
            mid = (l + h) >> 1
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            if nums[mid] == nums[mid + 1]:
                if mid % 2 == 0:
                    l = mid + 1
                else:
                    h = mid
            elif nums[mid] == nums[mid - 1]:
                if mid % 2 == 0:
                    h = mid
                else:
                    l = mid + 1
        return nums[l]