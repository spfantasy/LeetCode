class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """从左到右遍历，看看有没有 右>左+*的时刻"""
        l = 0
        r = 0
        m = 0
        for char in s:
            if char == '(':
                l += 1
            elif char == ')':
                r += 1
            elif char == '*':
                m += 1
            if l + m < r:
                return False
        """从右到左遍历，看看有没有 左>右+*的时刻"""
        l = 0
        r = 0
        m = 0
        for char in s[::-1]:
            if char == ')':
                l += 1
            elif char == '(':
                r += 1
            elif char == '*':
                m += 1
            if l + m < r:
                return False
        return True