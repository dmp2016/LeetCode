class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        return len([1 for c in s[:len(s) // 2].lower() if c in vowels]) == len([1 for c in s[len(s) // 2:].lower() if c in vowels])


test = Solution()
print(test.halvesAreAlike('book'))
print(test.halvesAreAlike('textbook'))
print(test.halvesAreAlike('MerryChristmas'))
print(test.halvesAreAlike('AbCdEfGh'))
print(test.halvesAreAlike('tkPAdxpMfJiltOerItiv'))
