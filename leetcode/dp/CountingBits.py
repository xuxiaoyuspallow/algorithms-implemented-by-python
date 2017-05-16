# coding:utf-8
"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's
in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n)
/possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_ popcount in c++ or in any other
language.
"""

"""
0    0000    0
-------------
1    0001    1
-------------
2    0010    1
3    0011    2
-------------
4    0100    1
5    0101    2
6    0110    2
7    0111    3
-------------
8    1000    1
9    1001    2
10   1010    2
11   1011    3
12   1100    2
13   1101    3
14   1110    3
15   1111    4

f[i] = f[i/2] + i % 2
"""


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]
        for i in range(1,num+1):
            result.append(result[i >> 2] + i % 2)
        return result

