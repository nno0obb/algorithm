"""
# 백준
# No. 2042
# Python 3.11.9
# by "nno0obb"
"""

import math
import sys


class SegmentTree:
    def __init__(self, A: list[int]) -> None:
        self.nums = A
        self.k = math.ceil(math.log2(len(A)))
        self.T = [0] * (2 ** (self.k + 1))
        for i, num in enumerate(A):
            self.T[i + 2**self.k] = num
        for i in range(2**self.k - 1, 0, -1):
            self.T[i] = self.T[2 * i] + self.T[2 * i + 1]

    def update(self, idx: int, num: int) -> None:
        self.nums[idx] = num
        cdx = idx + 2**self.k
        self.T[cdx] = num
        while cdx > 1:
            self.T[cdx // 2] = self.T[cdx] + self.T[cdx ^ 1]
            cdx //= 2

    def query(self, sdx: int, edx: int) -> int:
        ldx, rdx = sdx + 2**self.k, edx + 2**self.k
        ans = 0
        while ldx <= rdx:
            # pdx = ldx // 2
            # if (2*pdx + 1) == ldx:
            # 부모노드의 구간이 현재 질의구간을 벗어남
            # 따라서, 현재 노드의 구간까지의 질의구간을 구간합에 더하고
            # 부모노드 오른쪽 옆노드로 이동
            if ldx % 2 == 1:
                ans += self.T[ldx]
                ldx += 1

            # pdx = rdx // 2
            # if (2*pdx) == rdx:
            # 부모노드의 구간이 현재 질의구간을 벗어남
            # 따라서, 현재 노드의 구간가지의 질의구간을 구간합에 더하고
            # 부모노드의 왼쪽 옆노드로 이동
            if rdx % 2 == 0:
                ans += self.T[rdx]
                rdx -= 1
            ldx //= 2
            rdx //= 2
        return ans


def main():
    # Input
    N, M, K = map(int, input().split())
    A = [int(sys.stdin.readline().strip()) for _ in range(N)]
    Q = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M + K)]

    # Logic
    segment_tree = SegmentTree(A)
    for a, b, c in Q:
        if a == 1:
            segment_tree.update(b - 1, c)
        elif a == 2:
            print(segment_tree.query(b - 1, c - 1))


if __name__ == "__main__":
    main()
