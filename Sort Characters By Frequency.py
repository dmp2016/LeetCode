from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join([c * n for c, n in Counter(s).most_common()])        


test = Solution()
print(test.frequencySort('tree'))
print(test.frequencySort('cccaaa'))
print(test.frequencySort('Aabb'))
