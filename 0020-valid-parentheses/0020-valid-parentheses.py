class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {'(': ')', '[': ']', '{': '}'}

        for ch in s:
            if ch in mp:
                stack.append(ch)
            else:
                if not stack or mp[stack.pop()] != ch:
                    return False

        return not stack