class Solution:
    def reverseVowels(self, s: str) -> str:
        ind1, ind2 = 0, len(s) - 1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        res_left = []
        res_right = []
        while ind1 < ind2:
            if s[ind1] in vowels and s[ind2] in vowels:
                res_left.append(s[ind2])
                res_right.append(s[ind1])
                ind1 += 1
                ind2 -= 1
            elif s[ind1] not in vowels:
                res_left.append(s[ind1])
                ind1 += 1
            elif s[ind2] not in vowels:
                res_right.append(s[ind2])
                ind2 -= 1
        if ind1 == ind2:
            res_left.append(s[ind1])
        res_right.reverse()
        return ''.join(res_left) + ''.join(res_right)


test = Solution()
print(test.reverseVowels(s = "hello"))
print(test.reverseVowels(s = "leetcode"))
