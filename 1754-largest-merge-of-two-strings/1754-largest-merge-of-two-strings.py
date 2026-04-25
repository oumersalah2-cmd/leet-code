class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        merge = []

        while i < len(word1) and j < len(word2):
            # Compare remaining substrings
            if word1[i:] > word2[j:]:
                merge.append(word1[i])
                i += 1
            else:
                merge.append(word2[j])
                j += 1

        # Append remaining parts
        merge.append(word1[i:])
        merge.append(word2[j:])

        return ''.join(merge)
        