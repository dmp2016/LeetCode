from typing import List
from functools import lru_cache


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m = len(words[0])
        n = len(target)

        @lru_cache(None)
        def get_words_amount(dict_ind: int, cur_char_ind: int):
            cnt = 0
            for word in words:
                if word[dict_ind] == target[cur_char_ind]:
                    cnt += 1
            return cnt

        @lru_cache(None)
        def do_rec(dict_ind: int, cur_char_ind: int):
            if cur_char_ind == n:
                return 1
            if m - dict_ind < n - cur_char_ind:
                return 0

            res = get_words_amount(dict_ind, cur_char_ind) * do_rec(dict_ind + 1, cur_char_ind + 1) + \
                do_rec(dict_ind + 1, cur_char_ind)
            
            return res % 1000000007
        
        return do_rec(0, 0) % 1000000007


t = Solution()
print(t.numWays(words=["acca", "bbbb", "caca"], target="aba"))
print(t.numWays(words=["abba", "baab"], target="bab"))
