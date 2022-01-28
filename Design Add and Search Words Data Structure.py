from collections import defaultdict
from typing import List
import math


class WordDictionary:
    def __init__(self):
        self.data = []
        self.info = defaultdict(list)
        self.len_info = defaultdict(list)

    def addWord(self, word: str) -> None:
        self.data.append(word)
        self.len_info[len(word)].append(len(self.data) - 1)
        for ind in range(len(word)):
            self.info[(ind, word[ind])].append(len(self.data) - 1)

    def search(self, word: str) -> bool:
        if len(word) not in self.len_info:
            return False
        if word == '.' * len(word):
            return True
        key = None
        ms = math.inf
        for ind in range(len(word)):
            if (ind, word[ind]) in self.info and len(self.info[(ind, word[ind])]) < ms:
                ms = len(self.info[(ind, word[ind])])
                key = (ind, word[ind])
        if ms < len(self.len_info[len(word)]):
            ind_list = self.info[key]
        else:
            ind_list = self.len_info[len(word)]
        for ind in ind_list:
            if len(self.data[ind]) == len(word):
                if all(self.data[ind][i] == word[i] or word[i] == '.' for i in range(len(word))):
                    return True
        return False
