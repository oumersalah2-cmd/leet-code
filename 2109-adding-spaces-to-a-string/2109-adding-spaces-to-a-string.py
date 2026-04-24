class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        j = 0

        for i in range (len(s)):
            if j < len(spaces) and i == spaces[j]:
                result.append(" ")
                j += 1

            result.append(s[i])

        return "" .join(result)        