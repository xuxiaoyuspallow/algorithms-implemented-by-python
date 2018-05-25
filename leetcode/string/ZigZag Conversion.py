"""

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        if numRows == 2:
            res_1 = ''
            res_2 = ''
            for i in range(len(s)):
                if i % 2:
                    res_1 += s[i]
                else:
                    res_2 += s[i]
            return res_2 + res_1
        res = [''] * numRows
        index = 0
        direction = True  # 向下
        for i in s:
            if direction:
                res[index] += i
            else:
                res[numRows - 2 - index] += i
            if direction and index == numRows - 1:
                direction = False
                index = 0
            elif not direction and index <= numRows - 3:
                direction = True
                index = 0
            else:
                index += 1
        return ''.join(res)


Solution().convert("PAYPALISHIRING",4)