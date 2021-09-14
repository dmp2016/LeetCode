class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        rev = [c for c in s if 'a' <= c <= 'z' or 'A' <= c <= 'Z']
        return ''.join([rev.pop() if 'a' <= c <= 'z' or 'A' <= c <= 'Z' else c for c in s])


test = Solution()
print(test.reverseOnlyLetters(s="ab-cd"))
print(test.reverseOnlyLetters(s="a-bC-dEf-ghIj"))
print(test.reverseOnlyLetters(s="Test1ng-Leet=code-Q!"))
