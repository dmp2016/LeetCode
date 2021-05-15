class Solution:
    def isNumber(self, s: str) -> bool:
        if len(set(s.lower()).difference(['e', '+', '-', '.'] + list(map(str, range(0, 10))))) != 0:
            return False
        try:
            float(s)
            return True
        except Exception as e:
            return False
