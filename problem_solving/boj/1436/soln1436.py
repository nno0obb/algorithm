"""
# 백준
# No. 1436
# Python 3.11.9
# by "nno0obb"
"""

from collections import deque
from math import ceil, log10


def main():
    # Input
    N = int(input())

    # Logic
    que = deque()
    is_visited = set()

    que.append("666")
    is_visited.add(666)

    for _ in range(ceil(log10(N))):
        for _ in range(len(que)):
            c = que.popleft()
            for i in range(10):
                n1 = str(c) + str(i)
                n2 = str(i) + str(c)
                for n in [n1, n2]:
                    que.append(n)
                    is_visited.add(int(n))

    lst = list(is_visited)
    lst.sort()
    ans = lst[N - 1]

    # Output
    print(ans)


if __name__ == "__main__":
    main()
