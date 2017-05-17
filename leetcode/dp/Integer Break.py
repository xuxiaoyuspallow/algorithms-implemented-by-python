"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those
integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.
"""
from functools import reduce


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        from collections import defaultdict
        buff = defaultdict(list)
        buff[2] = [1,1]
        for i in range(3,n+1):
            add_flag = False
            temp = []
            for j in buff[i - 1]:
                if j == min(buff[i - 1]):
                    if not add_flag:
                        if j + 1 == 4:
                            temp.extend([2,2])
                        else:
                            temp.append(j + 1)
                        add_flag = True
                    else:
                        temp.append(j)
                else:
                    temp.append(j)
                buff[i] = temp
        return reduce(lambda x,y:x*y,buff[n])

if __name__ == '__main__':
    s = Solution()
    print(s.integerBreak(10))
