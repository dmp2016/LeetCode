class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:

        def check(a: int) -> bool:
            return str(a) == str(a)[::-1]

        def gen_pal() -> int:
            k = 1
            left_part = ''
            while True:
                left_part_max = '9' * (k >> 1)
                while True:
                    if k & 1:
                        for i in range(10):
                            yield int(left_part + str(i) + left_part[::-1])
                    else:
                        yield int(left_part + left_part[::-1])
                    if left_part == left_part_max:
                        break
                    else:
                        left_part = str(int(left_part) + 1)
                k += 1
                left_part = '1' + '0' * ((k >> 1) - 1)

        res = 0
        left = int(left)
        right = int(right)
        for a in gen_pal():
            b = a * a
            if b >= left:
                if b <= right:
                    if check(b):
                        res += 1
                else:
                    break

        return res


test = Solution()
print(test.superpalindromesInRange(4, 100000000))
