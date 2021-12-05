from typing import List


class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = words
        self.p = 0x7FFFFFFF
        self.x = 73513
        self.word_hash = [0] * len(self.words)
        self.possible_hash = set()
        for ind in range(len(self.words)):
            s = self.words[ind][::-1]
            self.word_hash[ind] = ord(s[0])
            self.possible_hash.add(self.word_hash[ind])
            for c in s[1:]:
                self.word_hash[ind] = (ord(c) + self.word_hash[ind] * self.x) & self.p
                self.possible_hash.add(self.word_hash[ind])

        self.word_hash_set = set(self.word_hash)
        self.stream = []
        self.word_max_len = max(len(w) for w in words)

    def query(self, letter: str) -> bool:
        letter = ord(letter)
        self.stream.append(letter)
        h = self.stream[-1]
        if h in self.word_hash_set:
            return True
        elif h not in self.possible_hash:
            return False
        for ind in range(2, min(self.word_max_len + 1, len(self.stream) + 1)):
            d = self.stream[-ind]
            h = (d + h * self.x) & self.p
            if h in self.word_hash_set:
                suf = ''.join(map(chr, self.stream[-ind:]))
                if any(w == suf for w in self.words):
                    return True
            elif h not in self.possible_hash:
                return False
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

words = ["cd", "f", "kl"]
obj = StreamChecker(words)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
for letter in letters:
    print(obj.query(letter))
