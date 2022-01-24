class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        is_first_lower = word[0].islower()
        is_remain_lower = True
        is_remain_cap = True
        for ind in range(1, len(word)):
            is_remain_lower = is_remain_lower and word[ind].islower()
            is_remain_cap = is_remain_cap and not word[ind].islower()
        return (not is_first_lower and (is_remain_lower or is_remain_cap)) or (is_first_lower and is_remain_lower)


test = Solution()
print(test.detectCapitalUse('USA'))
print(test.detectCapitalUse('FlaG'))
