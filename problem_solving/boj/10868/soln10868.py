"""
# 백준
# No. 10868
# Python 3.11.9
# by "nno0obb"
"""

import math
import sys
from typing import Optional


class SegmentTreeNode:
    def __init__(
        self,
        ldx: int,
        rdx: int,
        val: int = None,
        left: Optional["SegmentTreeNode"] = None,
        right: Optional["SegmentTreeNode"] = None,
    ) -> None:
        self.ldx = ldx
        self.rdx = rdx
        self.val = val
        self.left = left
        self.right = right


class SegmentTree:
    def __init__(self, nums: list[int]) -> None:
        self.nums = nums
        self.k = math.ceil(math.log2(len(nums)))
        self.root = self._build(0, len(nums) - 1)

    def _build(self, ldx: int, rdx: int) -> SegmentTreeNode:
        node = SegmentTreeNode(ldx, rdx)
        if ldx == rdx:
            node.val = self.nums[ldx]
            return node

        mid = (ldx + rdx) // 2
        node.left = self._build(ldx, mid)
        node.right = self._build(mid + 1, rdx)
        node.val = min(node.left.val, node.right.val)
        return node

    def update(self, node: Optional[SegmentTreeNode], idx: int, val: int) -> None:
        if not node:
            return

        if node.ldx == node.rdx:
            node.val = val
            return

        mdx = (node.ldx + node.rdx) // 2
        if idx <= mdx:
            self.update(node.left, idx, val)
        else:
            self.update(node.right, idx, val)
        node.val = min(node.left.val, node.right.val)

    def query(self, node: Optional[SegmentTreeNode], sdx: int, edx: int) -> int:
        if not node:
            return float("inf")
        elif sdx > node.rdx or edx < node.ldx:
            return float("inf")
        elif sdx <= node.ldx and edx >= node.rdx:
            return node.val
        else:
            return min(self.query(node.left, sdx, edx), self.query(node.right, sdx, edx))


def main():
    # Input
    N, M = map(int, input().split())
    nums = [int(sys.stdin.readline().strip()) for _ in range(N)]
    Q = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

    # Logic
    segment_tree = SegmentTree(nums)
    for a, b in Q:
        # Output
        print(segment_tree.query(segment_tree.root, a - 1, b - 1))


if __name__ == "__main__":
    main()
