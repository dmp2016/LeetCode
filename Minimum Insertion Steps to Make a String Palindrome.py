from functools import lru_cache

class Solution:
    def minInsertions(self, s: str) -> int:

        @lru_cache(None)
        def do_rec(left: int, right: int) -> int:
            if right - left <= 0:
                return 0
            if s[left] == s[right]:
                return do_rec(left + 1, right - 1)
            else:
                return min(do_rec(left, right - 1), do_rec(left + 1, right)) + 1
        
        return do_rec(0, len(s) - 1)


t = Solution()
# print(t.minInsertions(s="zzazz"))
# print(t.minInsertions(s="mbadm"))
# print(t.minInsertions(s="leetcode"))
print(t.minInsertions(s="tldjbqjdogipebqsohdypcxjqkrqltpgviqtqz"))
print(t.minInsertions(s="hroamwegvonydrclqxwddrwiejzqcokfwcbsqourfexoylnhookppmirgwfowjpirgbcvlwrxtqncxvjqurjxzzxiknmwzsuolfskosoopmtzwgzsoxcdicsvkyuowhicfdadqekagqtaggwxfkucyhoonrqtrgbhtvpidmvvnzzjbgneoeaumvgikqbndxvpsxgddnuvrwvzvhrtkuazoeppejxggpwpuzaxcdghmwvdawqyqmhtapocsshvfhpofclsrmtkgia"))
