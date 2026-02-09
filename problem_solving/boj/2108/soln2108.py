"""
# 백준
# No. 2108
# Python 3.11.9
# by "nno0obb"
"""

import sys
from collections import Counter


def main():
    # Input
    N = int(input())
    A = [int(sys.stdin.readline().strip()) for _ in range(N)]

    # Logic
    A.sort()
    avg = round(sum(A) / N)
    median = A[N // 2]
    counter = Counter(A)
    top_freq = counter.most_common(1)[0][1]
    modes = list(filter(lambda x: x[1] == top_freq, counter.most_common()))
    mode = modes[0][0] if len(modes) == 1 else sorted(modes)[1][0]
    _range = A[-1] - A[0]

    # Output
    print(avg)
    print(median)
    print(mode)
    print(_range)


if __name__ == "__main__":
    main()
