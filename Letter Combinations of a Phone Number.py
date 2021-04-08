from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if digits == '':
            return []
        res = ['']
        for c1 in digits:
            new_res = []
            for s in res:
                for c2 in letters[c1]:
                    new_res.append(s + c2)
            res = new_res
        return res


test = Solution()
print(test.letterCombinations(digits="23"))
print(test.letterCombinations(digits=""))
print(test.letterCombinations(digits="2"))
print(test.letterCombinations(digits="2222"))
