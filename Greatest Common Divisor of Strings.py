class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)
        for d in range(min(n1, n2), 0, -1):
            if n1 % d == 0 and n2 % d == 0:
                md = str1[:d]
                if str1 == md * (n1 // d) and str2 == md * (n2 // d):
                    return md
        return ''


test = Solution()
print(test.gcdOfStrings(str1="ABCABC", str2="ABC"))
print(test.gcdOfStrings(str1="ABABAB", str2="ABAB"))
print(test.gcdOfStrings(str1="LEET", str2="CODE"))
print(test.gcdOfStrings(str1="TAUXXTAUXXTAUXXTAUXXTAUXX",
      str2="TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))
