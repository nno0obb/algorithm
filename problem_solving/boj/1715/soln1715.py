"""
# 백준
# No. 1715
# Python 3.11.9
# by "nno0obb"
"""

import heapq
import sys


def main():
    # Input
    N = int(input())
    S = [int(sys.stdin.readline().strip()) for _ in range(N)]

    # Logic
    heapq.heapify(S)
    ans = 0

    while len(S) > 1:
        A = heapq.heappop(S)
        B = heapq.heappop(S)
        ans += A + B
        heapq.heappush(S, A + B)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
