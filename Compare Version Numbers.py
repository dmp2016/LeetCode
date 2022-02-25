class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        v1 = v1 + [0] * max(0, len(v2) - len(v1))
        v2 = v2 + [0] * max(0, len(v1) - len(v2))
        for a, b in zip(v1, v2):
            if a < b:
                return -1
            if a > b:
                return 1
        return 0


test = Solution()
print(test.compareVersion(version1="1.01", version2="1.001"))
print(test.compareVersion(version1="1.0", version2="1.0.0"))
print(test.compareVersion(version1="0.1", version2="1.1"))
