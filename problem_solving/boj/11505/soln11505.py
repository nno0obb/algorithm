"""
# 백준
# No. 11505
# Python 3.11.9
# by "nno0obb"
"""

import math
import sys

MOD = 1_000_000_007


class SegmentTree:
    def __init__(self, nums: list[int]) -> None:
        self.nums = nums
        self.k = math.ceil(math.log2(len(nums)))
        self.T = [0] * (2 ** (self.k + 1))
        for i, num in enumerate(nums):
            self.T[i + 2**self.k] = num
        for i in range(2**self.k - 1, 0, -1):
            self.T[i] = self.T[2 * i] * self.T[2 * i + 1] % MOD

    def update(self, idx: int, num: int) -> None:
        self.nums[idx] = num
        cdx = idx + 2**self.k
        self.T[cdx] = num
        while cdx > 1:
            self.T[cdx // 2] = self.T[cdx] * self.T[cdx ^ 1] % MOD
            cdx //= 2

    def query(self, sdx: int, edx: int) -> int:
        ldx, rdx = sdx + 2**self.k, edx + 2**self.k
        ans = 1
        while ldx <= rdx:
            if ldx % 2 == 1:
                ans *= self.T[ldx]
                ans %= MOD
                ldx += 1
            if rdx % 2 == 0:
                ans *= self.T[rdx]
                ans %= MOD
                rdx -= 1
            ldx //= 2
            rdx //= 2
        return ans


def main():
    # Input
    N, M, K = map(int, input().split())
    nums = [int(sys.stdin.readline().strip()) for _ in range(N)]
    queries = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M + K)]

    # Logic
    segment_tree = SegmentTree(nums)
    for a, b, c in queries:
        if a == 1:
            segment_tree.update(b - 1, c)
        elif a == 2:
            # Output
            print(segment_tree.query(b - 1, c - 1))


if __name__ == "__main__":
    main()
