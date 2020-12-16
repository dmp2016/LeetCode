class Solution:
    def nextGreaterElement(self, n: int) -> int:
        d_list = []
        while n > 0:
            d_list.append(n % 10)
            n //= 10
        if len(d_list) == 1:
            return -1
        ind = 1
        tail = [d_list[0]]
        max_tail = d_list[0]
        while ind < len(d_list):
            if max_tail > d_list[ind]:
                d_tail = min(filter(lambda x: x > d_list[ind], tail))
                tail_ind = tail.index(d_tail)
                d_list[ind], tail[tail_ind] = tail[tail_ind], d_list[ind]
                tail.sort()
                return(int(''.join(map(str, tail[::-1] + d_list[ind:]))[::-1]))
            max_tail = max(max_tail, d_list[ind])
            tail.append(d_list[ind])
            ind += 1
        return -1


test = Solution()
print(test.nextGreaterElement(61542332))
print(test.nextGreaterElement(12))
print(test.nextGreaterElement(21))
print(test.nextGreaterElement(333))
