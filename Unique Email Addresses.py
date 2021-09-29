from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            part1, part2 = email.split('@')
            res.add(f"{part1.replace('.', '').split('+')[0]}@{part2}")
        return len(res)


test = Solution()
print(test.numUniqueEmails(emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
print(test.numUniqueEmails(emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))
