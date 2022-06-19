from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        suf = 'z' * 3000
        res = []
        sw = ''
        for c in searchWord:
            sw += c
            ind1 = bisect_left(products, sw)
            ind2 = bisect_right(products, sw + suf)
            res.append(products[ind1:ind2][:3])
        return res


test = Solution()
print(test.suggestedProducts(products=["mobile", "mouse", "moneypot", "monitor", "mousepad"], searchWord="mouse"))
print(test.suggestedProducts(products=["havana"], searchWord="havana"))
print(test.suggestedProducts(products=["bags", "baggage", "banner", "box", "cloths"], searchWord="bags"))
