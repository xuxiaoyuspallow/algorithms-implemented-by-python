class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        - 若p为空，若s也为空，返回true，反之返回false
        - 若p的长度为1，若s长度也为1，且相同或是p为'.'则返回true，反之返回false
        - 若p的第二个字符不为*，若此时s为空返回false，否则判断首字符是否匹配，且从各自的第二个字符开始调用递归函数匹配
        - 若p的第二个字符为*，若s不为空且字符匹配，调用递归函数匹配s和去掉前两个字符的p，若匹配返回true，否则s去掉首字母
        - 返回调用递归函数匹配s和去掉前两个字符的p的结果
        """
        if not p:
            return not s
        if len(p) == 1:
            return len(s) == 1 and (p == '.' or s == p)
        if p[1] != '*':
            if not s: return False
            return (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:],p[1:])
        while (s and (s[0] == p[0] or p[0] == '.')):
            if self.isMatch(s, p[2:]):
                return True
            s = s[1:]
        return self.isMatch(s, p[2:])


print(Solution().isMatch('aab','c*a*b'))
