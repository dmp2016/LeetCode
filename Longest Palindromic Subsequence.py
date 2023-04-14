from functools import lru_cache
from bisect import bisect_left, bisect_right


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        char_ind = dict()
        for ind in range(len(s)):
            char_ind.setdefault(s[ind], []).append(ind)
        cache = dict()

        def do_rec(left: int, right: int) -> int:
            if (left, right) in cache:
                return cache[(left, right)]
            if left > right:
                return 0
            res = 1
            char_used = set()
            for ind_left in range(left, right + 1):
                char_left = s[ind_left]
                if char_left in char_used:
                    continue
                char_used.add(char_left)
                r = char_ind.get(char_left)
                if r and r[-1] > ind_left and r[0] < right:
                    ind_search = bisect_right(r, right)
                    if r[ind_search - 1] > ind_left:
                        res = max(res, do_rec(ind_left + 1, r[ind_search - 1] - 1) + 2)
            cache[(left, right)] = res
            return res

        return do_rec(0, len(s) - 1)


t = Solution()
print(t.longestPalindromeSubseq(s="bbbab"))
print(t.longestPalindromeSubseq(s="cbbd"))
print(t.longestPalindromeSubseq(s="a"))
print(t.longestPalindromeSubseq(s=""))
print(t.longestPalindromeSubseq(s="abcd"))
print(t.longestPalindromeSubseq(s="gphyvqruxjmwhonjjrgumxjhfyupajxbjgthzdvrdqmdouuukeaxhjumkmmhdglqrrohydrmbvtuwstgkobyzjjtdtjroqpyusfsbjlusekghtfbdctvgmqzeybnwzlhdnhwzptgkzmujfldoiejmvxnorvbiubfflygrkedyirienybosqzrkbpcfidvkkafftgzwrcitqizelhfsruwmtrgaocjcyxdkovtdennrkmxwpdsxpxuarhgusizmwakrmhdwcgvfljhzcskclgrvvbrkesojyhofwqiwhiupujmkcvlywjtmbncurxxmpdskupyvvweuhbsnanzfioirecfxvmgcpwrpmbhmkdtckhvbxnsbcifhqwjjczfokovpqyjmbywtpaqcfjowxnmtirdsfeujyogbzjnjcmqyzciwjqxxgrxblvqbutqittroqadqlsdzihngpfpjovbkpeveidjpfjktavvwurqrgqdomiibfgqxwybcyovysydxyyymmiuwovnevzsjisdwgkcbsookbarezbhnwyqthcvzyodbcwjptvigcphawzxouixhbpezzirbhvomqhxkfdbokblqmrhhioyqubpyqhjrnwhjxsrodtblqxkhezubprqftrqcyrzwywqrgockioqdmzuqjkpmsyohtlcnesbgzqhkalwixfcgyeqdzhnnlzawrdgskurcxfbekbspupbduxqxjeczpmdvssikbivjhinaopbabrmvscthvoqqbkgekcgyrelxkwoawpbrcbszelnxlyikbulgmlwyffurimlfxurjsbzgddxbgqpcdsuutfiivjbyqzhprdqhahpgenjkbiukurvdwapuewrbehczrtswubthodv"))
print(t.longestPalindromeSubseq(s="abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"))
