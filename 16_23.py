import collections
import functools
import random

import numpy as np


rand5 = functools.partial(random.randrange, 5)

numbers = np.arange(25).reshape((5, 5))


def rand7():
    row, col = rand5(), rand5()
    if (row * 5 + col) < 21:
        return numbers[row, col] // 3
    return rand7()


dist = [rand7() for _ in range(10000)]

print(sorted(collections.Counter(dist).items(), key=lambda item: item[0]))
