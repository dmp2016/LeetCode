import numpy as np
import itertools
import datetime as dt
from typing import List, Iterator
import pandas as pd

pd.isna()


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        pass


a = [0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1]

# max([len(list(g)) for k, g in itertools.groupby(a, lambda x: not x) if not k])


def get_len1(x):
    return max([len(list(g)) for k, g in itertools.groupby(a, lambda x: not x) if not k])


def get_len2(x):
    return max([len(p) for p in (''.join(map(str, a))).split('0')])


def calc_groups_length(seq: List[int], delimiter: int) -> Iterator[int]:
    group: List[int] = []
    for num in seq:
        if num != delimiter:
            group.append(num)
        elif group:
            yield len(group)
            group = []


tt = dt.datetime.utcnow()
for _ in range(1000000):
    get_len1(a)
print(dt.datetime.utcnow() - tt)

tt = dt.datetime.utcnow()
for _ in range(1000000):
    d = max(list(calc_groups_length(a + [0], 0)))
print(dt.datetime.utcnow() - tt)
