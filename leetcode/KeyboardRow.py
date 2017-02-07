"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American
keyboard like the image below.


American keyboard


Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
"""


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
            return []
        result = []
        for word in words:
            if self.verify(word.lower()):
                result.append(word)
        return result

    def verify(self,word):
        row1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        row2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        row3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        if word[0] in row1:
            flag = 1
        elif word[0] in row2:
            flag = 2
        else:
            flag = 3
        for w in word:
            if w in row1:
                c_flag = 1
            elif w in row2:
                c_flag = 2
            else:
                c_flag = 3
            if flag != c_flag:
                return False
        return True

